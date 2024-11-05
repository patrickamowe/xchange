from django.shortcuts import render
from convert.models import Currency
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .functions import fetch_top_headlines, fetch_everything

# APIs keys
api_key = "2d153877d4d14feca1be2288de02435a"

# Create your views here.


def index(request):
    currencies = Currency.objects.all()

    respond = fetch_top_headlines(api_key, "us")
    if respond.status_code == 200:
        data = respond.json()
        news = data["articles"]
        first_six_new = news[:8]
    else:
        first_six_new = list()

    return render(request, "convert/index.html", {"currencies":currencies, "news":first_six_new})


def news_view(request):

    respond = fetch_everything(api_key, "currency")
    if respond.status_code == 200:
        data = respond.json()
        news = data["articles"]
        first_six_new = news[:8]
    else:
        first_six_new = list()
    return render(request, "convert/news.html", {"news":first_six_new})

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