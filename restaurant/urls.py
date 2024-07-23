from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import privacy_policy


urlpatterns = [
    path('privacy', privacy_policy, name='privacy_policy'),
    path('', include('menu.urls')),
    
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
