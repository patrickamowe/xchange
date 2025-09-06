from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from convert.models import Currency, User, Wishlist, WishlistItem
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from convert.services import fetchNewsHeadline, fetchNews, pairsLiveRate
from decouple import config
from convert.config.constants import POPULAR_PAIRS, LIVE_PAIRS

def index(request):

    currencies = Currency.objects.all()
    currency_rates = pairsLiveRate(config('EXCHANGE_API'), LIVE_PAIRS)
    respond = fetchNewsHeadline(config('NEWS_API'), "us")

    if respond["status"] == "ok":
        news = respond["articles"]
        first_eight_news = news[:8]
    else:
        first_eight_news = []

    return render(request, "convert/index.html", {"currencies":currencies, "news":first_eight_news, "currency_rates":currency_rates, "popular_pairs":POPULAR_PAIRS})


def news_view(request):

    respond = fetchNews(config('NEWS_API'), "currency")
    if respond["status"] == "ok":
        news = respond["articles"]
        first_eight_news = news[:8]
    else:
        first_eight_news = []
    return render(request, "convert/news.html", {"news":first_eight_news})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, "convert/login.html")

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

    return render(request, "convert/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def available_currency_view(request):
    currencies = Currency.objects.all()

    return render(request, "convert/available_currency.html", {"currencies": currencies})

@login_required
def saved_currency_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    if not created:
        items = WishlistItem.objects.filter(wishlist=wishlist)
        currency_pairs = [{"base_code": item.base_currency.code, "target_code": item.quote_currency.code} for item in items]
        currency_rates = pairsLiveRate(config('EXCHANGE_API'), currency_pairs)
        wishlist_items = list(zip(items, currency_rates))
    else:
        wishlist_items = []

    return render(request, "convert/saved_currency.html", {"wishlist_items": wishlist_items})


# API views
@login_required
def add_wishlist(request, base_currency_code, quote_currency_code):
    try:
        wishlist, created_wishlist = Wishlist.objects.get_or_create(user=request.user)
        base_currency = Currency.objects.get(code=base_currency_code)
        quote_currency = Currency.objects.get(code=quote_currency_code)
        wishlist_item, created_wishlist_item = WishlistItem.objects.get_or_create(wishlist=wishlist, base_currency=base_currency, quote_currency=quote_currency)

        if created_wishlist or created_wishlist_item:
            response_data = {'status':'success', 'message': 'currency pair successfully added to wishlist'}
            return JsonResponse(response_data, status=201)
        else:
            response_data = {'status':'info', 'message': 'currency pair already in wishlist'}
            return JsonResponse(response_data, status=200)
    except Currency.DoesNotExist:
        response_data = {'status':'fail', 'message':'currency not found'}
        return JsonResponse(response_data, status=404)
    except Exception as e:
        response_data = {'status':'fail', 'message':str(e)}
        return JsonResponse(response_data, status=500)


@login_required
def remove_wishlist(request, base_currency_code, quote_currency_code):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    base_currency = get_object_or_404(Currency, code=base_currency_code)
    quote_currency = get_object_or_404(Currency, code=quote_currency_code)
    try:
        wishlist_item = WishlistItem.objects.get(wishlist=wishlist, base_currency=base_currency, quote_currency=quote_currency)
        wishlist_item.delete()
        response_data = {'status':'success', 'message':'currency pair deleted from wishlist successfully'}
        return JsonResponse(response_data, status=200)
    except WishlistItem.DoesNotExist:
        response_data = {'status': 'fail', 'message':'currency pair not found'}
        return JsonResponse(response_data, status=404)
    except Exception as e:
        response_data = {'status':'fail', 'message':str(e)}
        return JsonResponse(response_data, status=500)

