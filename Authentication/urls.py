from django.urls import path 
from django.contrib.auth.views import (
    LogoutView,
)
from Authentication.views import login

urlpatterns = [
    
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='authentication/logout.html'), name='logout'),
      
]


 