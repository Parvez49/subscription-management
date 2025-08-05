from django.shortcuts import render

from project_apps.subscriptions.models import Subscription


def subscription_list(request):
    subscriptions = Subscription.objects.select_related('user').all()
    return render(request, 'subscriptions/subscription_list.html', {
        'subscriptions': subscriptions
    })
