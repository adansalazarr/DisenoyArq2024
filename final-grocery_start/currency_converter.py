import requests

#API conversor
class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key #constructor para KEY

    def convert_currency(self, amount, from_currency, to_currency):
        url = f'http://api.exchangeratesapi.io/v1/latest' #obtiene valor más reciente en base a API
        params = { #peremetros que se envian por HTTP
            'access_key': self.api_key,
            'symbols': f'{from_currency},{to_currency}',
        }

        #guardamos la respuestas de la API
        response = requests.get(url, params=params) 
        rates = response.json().get('rates', {}) 
        from_rate = rates.get(from_currency)
        to_rate = rates.get(to_currency)

        # convetimos a dolares el orginal
        amount_in_usd = amount / from_rate
        converted_amount = amount_in_usd * to_rate
        return converted_amount
