from django.urls import path
from project_apps.subscriptions.views import subscription_list

urlpatterns = [
    path('subscriptions/', subscription_list, name='subscription_list'),
]
