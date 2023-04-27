from django.urls import path 
from Accessories.views import (
    # accessories
    CreateAccessories,
    DetailAccessories,
    ListAccessories,
    UpdateAccessories,
    DeleteAccessories,
    
    #accessories enquires 
    ListAccessoriesEnquiryAttendedTo,
    ListAccessoriesEnquiryNotAttendedTo,
    DeleteAccessoriesEnquiry,
    DetailAccessoriesEnquiry,
    
    # search
    AccessoriesAttendedToEnquirySearch,
    AccessoriesNotAttendedToEnquirySearch
)

urlpatterns = [
     # accessories
     path('create-accessory/', CreateAccessories.as_view(), name='create-accessory'),
     path('list-accessory/', ListAccessories.as_view(), name='list-accessory'),
     path('update-accessory/<int:pk>/<slug:slug>', UpdateAccessories.as_view(), name='update-accessory'),
     path('delete-accessory/<int:pk>/<slug:slug>', DeleteAccessories.as_view(), name='delete-accessory'),
     path('detail-accessory/<int:pk>/<slug:slug>', DetailAccessories.as_view(), name='detail-accessory'),
     
     #accessories enquires 
     path('list-accessory-enquiry-attended-to/', ListAccessoriesEnquiryAttendedTo.as_view(), name='list-accessory-attended-to'),
     path('list-accessory-enquiry-not-attended-to/', ListAccessoriesEnquiryNotAttendedTo.as_view(), name='list-accessory-not-attended-to'),
     path('delete-accessory-enquiry/<int:pk>/<slug:slug>', DeleteAccessoriesEnquiry.as_view(), name='delete-accessory-enquiry'),
     
     path('detail-accessory-enquiry/<int:pk>/<slug:slug>', DetailAccessoriesEnquiry.as_view(), name='detail-accessory-enquiry'),
     
     
      # search
    path('search-list-accessory-enquiry-attended-to/', AccessoriesAttendedToEnquirySearch.as_view(), name='search-list-accessory-attended-to'),
     path('search-list-accessory-enquiry-not-attended-to/', AccessoriesNotAttendedToEnquirySearch.as_view(), name='search-list-accessory-not-attended-to'),
 
     
     
     
      
]


 