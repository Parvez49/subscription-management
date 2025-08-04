from django.urls import include, path

app_name = 'subscriptions'

urlpatterns = [
    path('v1/', include('project_apps.subscriptions.api.v1.urls')),
]
