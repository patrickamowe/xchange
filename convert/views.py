from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from convert.models import Currency, User, SavedConversion, RecentConversion
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from convert.services.service import fetchNewsHeadline, fetchNews, pairsLiveRate
from decouple import config
from convert.constants.constant import POPULAR_PAIRS, LIVE_PAIRS

def index(request):

    currencies = Currency.objects.all()
    currency_rates = pairsLiveRate(config('EXCHANGE_API'), LIVE_PAIRS)
    response = fetchNewsHeadline(config('NEWS_API'), "us")

    if response.get("status") == "ok":
        news = response.get("articles", [])[:8]
    else:
        news = []

    return render(request, "index.html", {"currencies":currencies, "news":news, "currency_rates":currency_rates, "popular_pairs":POPULAR_PAIRS})


def news_view(request):
    query = request.GET.get("query") or "currency"

    response = fetchNews(config("NEWS_API"), query)
    if response.get("status") == "ok":
        news = response.get("articles", [])
    else:
        news = []

    return render(request, "news.html", {"news": news})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, "login.html")

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmation_password = request.POST.get('confirmation-password')

        if password == confirmation_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered.')
            else:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'Account created successfully. Please login.')
                    return redirect('login')
                except:
                    messages.error(request, 'Unable to create your account.')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, "register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def available_currency_view(request):
    currencies = Currency.objects.all()

    return render(request, "available_currency.html", {"currencies": currencies})

@login_required(login_url='login')
def saved_conversion_view(request):
    items = SavedConversion.objects.filter(user=request.user)
    currency_pairs = [{"base_code": item.base.code, "target_code": item.quote.code} for item in items]
    currency_rates = pairsLiveRate(config('EXCHANGE_API'), currency_pairs)
    saved_conversions = list(zip(items, currency_rates))

    return render(request, "saved_conversion.html", {"saved_conversions": saved_conversions})

def about_view(request):
    return render(request, "about.html")

@login_required(login_url='login')
def profile_view(request):
    user = request.user
    saved_pairs = SavedConversion.objects.filter(user=user)
    recent_pairs = RecentConversion.objects.filter(user=user)

    return render(request, "profile.html", {"user": user, "saved_pairs": saved_pairs, "recent_pairs": recent_pairs})


# API views
@login_required
def add_conversion(request, base_code, quote_code):
    try:
        
        base_currency = Currency.objects.get(code=base_code)
        quote_currency = Currency.objects.get(code=quote_code)
        saved_conversion, created_saved_conversion = SavedConversion.objects.get_or_create(user=request.user, base=base_currency, quote=quote_currency)

        if created_saved_conversion:
            response_data = {'status':'success', 'message': 'currency pair successfully added to saved conversion'}
            return JsonResponse(response_data, status=201)
        else:
            response_data = {'status':'info', 'message': 'currency pair already in saved conversion'}
            return JsonResponse(response_data, status=200)
    except Currency.DoesNotExist:
        response_data = {'status':'fail', 'message':'currency not found'}
        return JsonResponse(response_data, status=404)
    except Exception as e:
        response_data = {'status':'fail', 'message':str(e)}
        return JsonResponse(response_data, status=500)


@login_required
def remove_conversion(request, base_code, quote_code):
    base_currency = get_object_or_404(Currency, code=base_code)
    quote_currency = get_object_or_404(Currency, code=quote_code)
    try:
        saved_conversion = SavedConversion.objects.get(user=request.user, base=base_currency, quote=quote_currency)
        saved_conversion.delete()
        response_data = {'status':'success', 'message':'currency pair deleted from saved conversion successfully'}
        return JsonResponse(response_data, status=200)
    except SavedConversion.DoesNotExist:
        response_data = {'status': 'fail', 'message':'currency pair not found'}
        return JsonResponse(response_data, status=404)
    except Exception as e:
        response_data = {'status':'fail', 'message':str(e)}
        return JsonResponse(response_data, status=500)
    
@login_required
def clear_recent_conversions(request):
    try:
        RecentConversion.objects.filter(user=request.user).delete()
        response_data = {'status':'success', 'message':'all recent conversions cleared successfully'}
        return JsonResponse(response_data, status=200)
    except Exception as e:
        response_data = {'status':'fail', 'message':str(e)}
        return JsonResponse(response_data, status=500)
    
@login_required
def add_recent_conversion(request, base_code, quote_code):

    try:
        base_currency = Currency.objects.get(code=base_code)
        quote_currency = Currency.objects.get(code=quote_code)
        _, created_recent_conversion = RecentConversion.objects.get_or_create(user=request.user, base=base_currency, quote=quote_currency)

        if created_recent_conversion:

            # Limit to 5 recent conversions
            recent_conversions = RecentConversion.objects.filter(user=request.user)
            if recent_conversions.count() > 5:
                to_delete = recent_conversions[5:]
                to_delete.delete()

            response_data = {'status':'success', 'message': 'currency pair successfully added to recent conversion'}
            return JsonResponse(response_data, status=201)
        else:
            response_data = {'status':'info', 'message': 'currency pair already in recent conversion'}
            return JsonResponse(response_data, status=200)
    except Currency.DoesNotExist:
        response_data = {'status':'fail', 'message':'currency not found'}
        return JsonResponse(response_data, status=404)
    except Exception as e:
        response_data = {'status':'fail', 'message':str(e)}
        return JsonResponse(response_data, status=500)


def get_api_key(request):
    response_data = {'api_key': config('EXCHANGE_API')}
    return JsonResponse(response_data)