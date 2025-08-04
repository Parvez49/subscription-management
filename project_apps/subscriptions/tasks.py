from celery import shared_task
from project_apps.subscriptions.models import ExchangeRateLog
from project_apps.subscriptions.enums import CurrencyUnit
from project_apps.subscriptions.utils import fetch_exchange_rate


@shared_task
def fetch_usd_to_bdt_rate():
    try:
        rate = fetch_exchange_rate(CurrencyUnit.USD, CurrencyUnit.BDT)
        if rate:
            ExchangeRateLog.objects.create(
                base_currency=CurrencyUnit.USD,
                target_currency=CurrencyUnit.BDT,
                rate=rate
            )
            return f"Saved USD to BDT rate: {rate}"
        return "BDT rate not found"
    except Exception as e:
        return f"Error: {str(e)}"
