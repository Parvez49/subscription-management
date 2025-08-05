from django.urls import include, path

app_name = 'accounts'

urlpatterns = [
    path('v1/', include('project_apps.accounts.api.v1.urls')),
]