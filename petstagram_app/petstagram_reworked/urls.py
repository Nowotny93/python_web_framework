from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram_reworked.common.urls')),
    path('pets/', include('petstagram_reworked.pets.urls')),
    path('accounts/', include('petstagram_reworked.accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
