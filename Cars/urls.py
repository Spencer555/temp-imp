from django.urls import path

from Cars.views import (
    # cars
    CreateCarView,
    ListCarView,
    DeleteCarView,
    DetailCarView,
    UpdateCarView,
    
    # enquriy
    ListCarEnquiryAttendedTo,
    ListCarEnquiryNotAttendedTo,
    DeleteCarEnquiry,
    DetailCarEnquiry,
    
    # search
    CarAttendedToEnquirySearch,
    CarNotAttendedToEnquirySearch,
)

urlpatterns = [
    # cars
    path("create-car/", CreateCarView.as_view(), name="create-car"),
    path("", ListCarView.as_view(), name="list-car"),
    path(
        "detail-car/<slug:slug>/<int:pk>/", DetailCarView.as_view(), name="detail-car"
    ),
    path(
        "update-car/<slug:slug>/<int:pk>/", UpdateCarView.as_view(), name="update-car"
    ),
    path(
        "delete-car/<slug:slug>/<int:pk>/", DeleteCarView.as_view(), name="delete-car"
    ),
    
    # enquiry
    path(
        "list-car-enquiry-attended-to/",
        ListCarEnquiryAttendedTo.as_view(),
        name="list-car-enquiry-attended-to",
    ),
    path(
        "list-car-enquiry-not-attended-to/",
        ListCarEnquiryNotAttendedTo.as_view(),
        name="list-car-enquiry-not-attended-to",
    ),
   
    path(
        "detail-car-enquiry/<slug:slug>/<int:pk>/",
        DetailCarEnquiry.as_view(),
        name="detail-car-enquiry",
    ),
    path(
        "delete-car-enquiry/<slug:slug>/<int:pk>/",
        DeleteCarEnquiry.as_view(),
        name="delete-car-enquiry",
    ),
    
    # search
    path(
        "search-car-enquiry-not-attended-to/",
        CarNotAttendedToEnquirySearch.as_view(),
        name="search-car-enquiry-not-attended-to",
    ),
    path(
        "search-car-enquiry-attended-to/",
        CarAttendedToEnquirySearch.as_view(),
        name="search-car-enquiry-attended-to",
    ),
]
