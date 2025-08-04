from django.urls import path

from project_apps.subscriptions.api.v1.views import SubscribeCreateAPIView, SubscriptionListAPIView, \
    CancelSubscriptionAPIView, ExchangeRateRetrieveAPIView

app_name = 'v1'

urlpatterns = [
    path('subscribe/', SubscribeCreateAPIView.as_view(), name='subscribe'),
    path('subscriptions/', SubscriptionListAPIView.as_view(), name='subscriptions'),
    path('cancel/', CancelSubscriptionAPIView.as_view(), name='cancel-subscription'),
    path('exchange-rate/', ExchangeRateRetrieveAPIView.as_view(), name='exchange-rate'),
]
