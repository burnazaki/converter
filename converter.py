import requests


def convert_currency(price_in_usd, to_currency):

    TO_CURRENCIES = ('UAH', 'EUR', 'GBP')
    FROM_CURRENCY = "USD"

    if price_in_usd <= 0:
        raise ValueError('Invalid price value: below or equal zero')

    elif to_currency not in TO_CURRENCIES:
        raise ValueError("Unsupported 'to_currency': %s" % to_currency)

    query = FROM_CURRENCY + '_' + to_currency
    URL = 'https://free.currencyconverterapi.com/api/v5/convert?q=' + query + '&compact=ultra'
    response = requests.get(URL)

    if response.status_code != 200:
        raise IOError('Request error: %s' % response.reason)

    data = response.json()

    result = price_in_usd * data.get(query)

    print(price_in_usd, "USD", " equals to ", result, to_currency)

    return result


convert_currency(price_in_usd=10, to_currency='UAH')
