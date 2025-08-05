from django.urls import path
from django.urls import path
from project_apps.accounts.api.v1.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'v1'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
