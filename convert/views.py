from django.shortcuts import render
from convert.models import Currency
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def index(request):
    currencies = Currency.objects.all()

    return render(request, "convert/index.html", {"currencies":currencies})


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