from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from payment import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
   path('payment/', include('payment.urls')),
  # This must be correct
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
