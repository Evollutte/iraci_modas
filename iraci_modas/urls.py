from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.core.views import view_404
handler404 = view_404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('apps.accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
