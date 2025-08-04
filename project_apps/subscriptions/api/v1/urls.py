from django.urls import path

from project_apps.subscriptions.api.v1.views import SubscribeCreateAPIVIEW, SubscriptionListAPIVIEW, CancelSubscriptionAPIVIEW

app_name = 'v1'

urlpatterns = [
    path('subscribe/', SubscribeCreateAPIVIEW.as_view(), name='subscribe'),
    path('subscriptions/', SubscriptionListAPIVIEW.as_view(), name='subscriptions'),
    path('cancel/', CancelSubscriptionAPIVIEW.as_view(), name='cancel-subscription'),
]
