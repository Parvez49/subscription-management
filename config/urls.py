"""
URL configuration for archive2024 project.

For more information please see:
https://docs.djangoproject.com/en/dev/topics/http/urls/
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

api_url_patterns = (
    [

    ], 'api'
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # api documentation
    path('schema/', SpectacularAPIView.as_view(api_version='v1'), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # api
    path('api/', include(api_url_patterns)),
    path('api_auth/', include('rest_framework.urls')),

    # Media files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

if settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
