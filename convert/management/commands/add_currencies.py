from django.core.management.base import BaseCommand
from convert.models import Currency
from convert.constants.constants import CURRENCY_STRINGS as strings

def creating_currency_list(input_string):
    # Initialize an empty list to hold the dictionaries
    currency_list = []
    input_strings = input_string

    # Process each line
    for line in input_strings.strip().split('\n'):
        # Find the start positions of 'code:', 'name:', and 'country:'
        code_start = line.index('code:') + len('code:')
        name_start = line.index('name:') + len('name:')
        country_start = line.index('country:') + len('country:')

        # Extract the segments between the keywords
        code = line[code_start:name_start - len('name:')].strip()
        name = line[name_start:country_start - len('country:')].strip()
        country = line[country_start:].strip()

        # Create a dictionary for each line
        currency_dict = {
            'code': code,
            'name': name,
            'country': country
        }

        # Append the dictionary to the list
        currency_list.append(currency_dict)

    return currency_list


class Command(BaseCommand):
    help = 'Add predefined currencies to the Currency table'

    def handle(self, *args, **options):
        currencies = creating_currency_list(strings)
        print(len(currencies))

        for currency in currencies:
            obj, created = Currency.objects.get_or_create(code=currency['code'], country=currency['country'], defaults={'name': currency['name']})
            if created:
                self.stdout.write(self.style.SUCCESS(f'Added {currency["name"]}'))
            else:
                self.stdout.write(f'{currency["name"]} already exists')
