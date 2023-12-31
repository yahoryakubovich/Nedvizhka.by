from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', NedvizhkaView.as_view(), name='nedvizhka'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('sale/', include('sale.urls')),
    path('accounts/profile/', include('user_profile.urls')),
    path('api/', include('api.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
