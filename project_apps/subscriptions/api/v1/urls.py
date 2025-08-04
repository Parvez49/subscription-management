from django.urls import path

from project_apps.subscriptions.api.v1.views import SubscribeAPIVIEW

app_name = 'v1'

urlpatterns = [
    path('subscribe/', SubscribeAPIVIEW.as_view(), name='subscribe'),
]
