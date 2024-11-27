from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from convert.models import Currency, User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
import json
from .querys import fetch_top_headlines, fetch_everything, get_live_rate

# APIs keys
api_key = "2d153877d4d14feca1be2288de02435a"

# Create your views here.


def index(request):
    currencies = Currency.objects.all()
    currency_rates = get_live_rate()

    respond = fetch_top_headlines(api_key, "us")
    if respond["status"] == "ok":
        news = respond["articles"]
        first_eight_news = news[:8]
    else:
        first_eight_news = []

    return render(request, "convert/index.html", {"currencies":currencies, "news":first_eight_news, "currency_rates":currency_rates})


def news_view(request):

    respond = fetch_everything(api_key, "currency")
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
        username = request.POST['username']
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        password = request.POST['password']
        confirmation_password = request.POST['confirmation-password']

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


# API functions
@csrf_exempt
def store_currency_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            CurrencyData.objects.create(
                base_currency=data['base_currency'],
                target_currency=data['target_currency'],
                exchange_rate=data['exchange_rate']
            )
            return JsonResponse({'message': 'Data stored successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

