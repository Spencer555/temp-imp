from django.urls import path 
from Readonly.views import (
    TermsAndCondtions,
    Privacy
        
)
urlpatterns = [
    
     path('terms-and-conditions/', TermsAndCondtions.as_view(), name='terms-and-conditions'),
     path('privacy/', Privacy.as_view() , name='privacy'),
       
]


 