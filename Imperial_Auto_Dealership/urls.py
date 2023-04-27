 
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render  
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('Authentication.urls')),
    path('accessories/', include('Accessories.urls')),
    path('', include('Cars.urls')),
    path('search/', include('GeneralSearch.urls')),
    path('our_services/', include('OurServices.urls')),
    path('readonly/', include('Readonly.urls')),
    path('analytics/', include('Analytics.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  