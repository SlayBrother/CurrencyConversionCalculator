import requests

def is_valid_currency(currency):
    """This will check to see that the currency you're attempting to convert from or to is a three letter currency"""
    return len(currency) == 3

def is_valid_amount(amount):
    """This function will check to see if the amount you're attempting to convert is above zero. The converter will not convert negative amounts nor 0. """
    try:
        amount_value = float(amount)
        return amount_value > 0
    except ValueError:
        return False

def get_converted_amount(convertfrom, convertto, amount):
    """This function is simply setting the values to call later"""
    url = f'https://api.exchangerate.host/convert?from={convertfrom}&to={convertto}&amount={amount}'
    response = requests.get(url)
    data = response.json()
    converted_amount = data['result']
    if converted_amount is not None:
        converted_amount = round(converted_amount, 2)
    return converted_amount, data['query']['to']