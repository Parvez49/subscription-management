import requests
from django.conf import settings


def fetch_exchange_rate(base: str, target: str) -> float:
    api_key = settings.EXCHANGE_RATE_API_KEY
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{base}/{target}'

    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Invalid API response")

    data = response.json()
    if data.get('result') == 'error' or 'conversion_rate' not in data:
        raise ValueError("Target currency not found or invalid data")

    return data['conversion_rate']
