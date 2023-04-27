from django.urls import path
from OurServices.views import (
    # contact enquires
    DeleteContactUsForEnquires,
    DetailContactUsForEnquires,
    ListContactUsForEnquiresAttended,
    ListContactUsForEnquiresNotAttended,
    # contact enquires search
    ContactEnquiryAttendedToEnquirySearch,
    ContactEnquiryNotAttendedToEnquirySearch,
    # let us sell your car
    CreateLetUsSellYourCar,
    DeleteLetUsSellYourCar,
    DetailLetUsSellYourCar,
    ListLetUsSellYourCarAttendedTo,
    ListLetUsSellYourCarNotAttendedTo,
    # let us sell your car search
    LetUsSellYourCarSearchAttendedTo,
    LetUsSellYourCarSearchNotAttendedTo,
    # ship car for us to sell
    CreateShipCarForUsSell,
    DeleteShipCarForUsSell,
    DetailShipCarForUsSell,
    ListShipCarForUsSellAttendedTo,
    ListShipCarForUsSellNotAttendedTo,
    # ship car for us to sell search
    ShipCarForUsSellSearchAttendedTo,
    ShipCarForUsSellSearchNotAttendedTo,
    # car rentals
    CreateCarRentals,
    DeleteCarRentals,
    ListCarRentals,
    UpdatCarRentals,
    DetailCarRentals,
    # rent car
    ListRentCarNotAttendedTo,
    ListRentCarAttendedTo,
    DeleteRentCar,
    DetailRentCar,
    # search rent car
    RentCarSearchAttendedTo,
    RentCarSearchNotAttendedTo,
    ServicesHome,
    # Accessories Listing
    DeleteListAccessories,
    DetailListAccessories,
    ListAccessoriesApproved,
    ListAccessoriesUnApproved,
    # Accessories Listing search
    SearchApprovedListAccessories,
    SearchUnApprovedListAccessories,
    #  Driving Sch Listing
    DeleteListDrivingSch,
    DetailListDrivingSch,
    ListDrivingSchApproved,
    ListDrivingSchUnApproved,
    #  Driving Sch Listing Search
    SearchUnApprovedListDrivingSch,
    SearchApprovedListDrivingSch,
    #  Driving Student Listing
    DetailRequestDrivingSch,
    DeleteRequestDrivingSch,
    RequestDrivingSchApproved,
    RequestDrivingSchUnApproved,
    #  Driving Student Listing Search
    SearchApprovedRequestDrivingSch,
    SearchUnApprovedRequestDrivingSch,
    #  Listing car rental
    DetailListingCarRental,
    DeleteListingCarRental,
    ListingCarRentalApproved,
    ListingCarRentalUnApproved,
    #  Listing car rental search
    SearchApprovedListingCarRental,
    SearchUnApprovedListingCarRental,
)

urlpatterns = [
    # contact enquires
    path(
        "list-contact-enquiry-attended-to/",
        ListContactUsForEnquiresAttended.as_view(),
        name="list-contact-enquiry-attended-to",
    ),
    path(
        "list-contact-enquiry-not-attended-to/",
        ListContactUsForEnquiresNotAttended.as_view(),
        name="list-contact-enquiry-not-attended-to",
    ),
    path(
        "detail-contact-enquiry-to/<int:pk>/<slug:slug>/",
        DetailContactUsForEnquires.as_view(),
        name="detail-contact-enquiry-to",
    ),
    path(
        "delete-contact-enquiry-not-attended-to/<int:pk>/<slug:slug>/",
        DeleteContactUsForEnquires.as_view(),
        name="delete-contact-enquiry-not-attended-to",
    ),
    # contact enquires search
    path(
        "search-contact-enquiry-attended-to/",
        ContactEnquiryAttendedToEnquirySearch.as_view(),
        name="search-contact-enquiry-attended-to",
    ),
    path(
        "search-contact-enquiry-not-attended-to/",
        ContactEnquiryNotAttendedToEnquirySearch.as_view(),
        name="search-contact-enquiry-not-attended-to",
    ),
    # let us sell your car
    path(
        "delete-sell-your-car/<int:pk>/<slug:slug>/",
        DeleteLetUsSellYourCar.as_view(),
        name="delete-sell-your-car",
    ),
    path(
        "detail-sell-your-car/<int:pk>/<slug:slug>/",
        DetailLetUsSellYourCar.as_view(),
        name="detail-sell-your-car",
    ),
    path(
        "create-sell-your-car/",
        CreateLetUsSellYourCar.as_view(),
        name="create-sell-your-car",
    ),
    path(
        "list-sell-your-car-not-attended-to/",
        ListLetUsSellYourCarNotAttendedTo.as_view(),
        name="sell-your-car-not-attended-to",
    ),
    path(
        "list-sell-your-car-attended-to/",
        ListLetUsSellYourCarAttendedTo.as_view(),
        name="sell-your-car-attended-to",
    ),
    # let us sell your car search
    path(
        "search-list-sell-your-car-not-attended-to/",
        LetUsSellYourCarSearchNotAttendedTo.as_view(),
        name="search-list-sell-your-car-not-attended-to",
    ),
    path(
        "search-list-sell-your-car-attended-to/",
        LetUsSellYourCarSearchAttendedTo.as_view(),
        name="search-list-sell-your-car-attended-to",
    ),
    # ship car for us to sell
    path(
        "delete-ship-car-for-sell/<int:pk>/<slug:slug>/",
        DeleteShipCarForUsSell.as_view(),
        name="delete-ship-car-for-sell",
    ),
    path(
        "detail-ship-car-for-sell/<int:pk>/<slug:slug>/",
        DetailShipCarForUsSell.as_view(),
        name="detail-ship-car-for-sell",
    ),
    path("create-ship-car/", CreateShipCarForUsSell.as_view(), name="create-ship-car"),
    path(
        "list-ship-car-not-attended-to/",
        ListShipCarForUsSellNotAttendedTo.as_view(),
        name="list-ship-car-not-attended-to",
    ),
    path(
        "list-ship-car-attended-to/",
        ListShipCarForUsSellAttendedTo.as_view(),
        name="list-ship-car-attended-to",
    ),
    # ship car for us to sell search
    path(
        "search-ship-car-not-attended-to/",
        ShipCarForUsSellSearchNotAttendedTo.as_view(),
        name="search-ship-car-not-attended-to",
    ),
    path(
        "search-ship-car-attended-to/",
        ShipCarForUsSellSearchAttendedTo.as_view(),
        name="search-ship-car-attended-to",
    ),
    # car rentals
    path("create-car-rental/", CreateCarRentals.as_view(), name="create-car-rental"),
    path("list-car-rental/", ListCarRentals.as_view(), name="list-car-rental"),
    path(
        "detail-car-rental/<slug:slug>/<int:pk>/",
        DetailCarRentals.as_view(),
        name="detail-car-rental",
    ),
    path(
        "delete-car-rental/<slug:slug>/<int:pk>/",
        DeleteCarRentals.as_view(),
        name="delete-car-rental",
    ),
    path(
        "update-car-rental/<slug:slug>/<int:pk>/",
        UpdatCarRentals.as_view(),
        name="update-car-rental",
    ),
    # rent car
    path(
        "delete-car-rent/<slug:slug>/<int:pk>/",
        DeleteRentCar.as_view(),
        name="delete-car-rent",
    ),
    path(
        "detail-car-rent/<slug:slug>/<int:pk>/",
        DetailRentCar.as_view(),
        name="detail-car-rent",
    ),
    path(
        "list-car-rent-enquiry-attended-to/ ",
        ListRentCarAttendedTo.as_view(),
        name="list-car-rent-enquiry-attended-to",
    ),
    path(
        "list-car-rent-enquiry-not-attended-to/ ",
        ListRentCarNotAttendedTo.as_view(),
        name="list-car-rent-enquiry-not-attended-to",
    ),
    # search rent car
    path(
        "search-car-rent-attended/ ",
        RentCarSearchAttendedTo.as_view(),
        name="search-car-rent-attended",
    ),
    path(
        "search-car-rent-not-attended/ ",
        RentCarSearchNotAttendedTo.as_view(),
        name="search-car-rent-not-attended",
    ),
    # services home
    path("services-home/ ", ServicesHome.as_view(), name="services-home"),
    # Accessories Listing
    path(
        "list-approved-accessories/",
        ListAccessoriesApproved.as_view(),
        name="list-approved-accessories",
    ),
    path(
        "list-unapproved-accessories/",
        ListAccessoriesUnApproved.as_view(),
        name="list-unapproved-accessories",
    ),
    path(
        "detail-list-accessories/<int:pk>/<slug:slug>/",
        DetailListAccessories.as_view(),
        name="detail-list-accessories",
    ),
    path(
        "delete-list-accessories/<int:pk>/<slug:slug>/",
        DeleteListAccessories.as_view(),
        name="delete-list-accessories",
    ),
    # Accessories Listing search
    path(
        "search-list-approved-accessories/",
        SearchApprovedListAccessories.as_view(),
        name="search-list-approved-accessories",
    ),
    path(
        "search-list-unapproved-accessories/",
        SearchUnApprovedListAccessories.as_view(),
        name="search-list-unapproved-accessories",
    ),
    # Driving Sch Listing
    path(
        "list-approved-drv-sch/",
        ListDrivingSchApproved.as_view(),
        name="list-approved-drv-sch",
    ),
    path(
        "list-unapproved-drv-sch/",
        ListDrivingSchUnApproved.as_view(),
        name="list-unapproved-drv-sch",
    ),
    path(
        "detail-list-drv-sch/<int:pk>/<slug:slug>/",
        DetailListDrivingSch.as_view(),
        name="detail-list-drv-sch",
    ),
    path(
        "delete-list-drv-sch/<int:pk>/<slug:slug>/",
        DeleteListDrivingSch.as_view(),
        name="delete-list-drv-sch",
    ),
    #  Driving Sch Listing Search
    path(
        "search-list-approved-drv-sch/",
        SearchApprovedListDrivingSch.as_view(),
        name="search-list-approved-drv-sch",
    ),
    path(
        "search-list-unapproved-drv-sch/",
        SearchUnApprovedListDrivingSch.as_view(),
        name="search-list-unapproved-drv-sch",
    ),
    #  Driving Student Listing
    path(
        "approved-req-drv-sch/",
        RequestDrivingSchApproved.as_view(),
        name="approved-req-drv-sch",
    ),
    path(
        "unapproved-req-drv-sch/",
        RequestDrivingSchUnApproved.as_view(),
        name="unapproved-req-drv-sch",
    ),
    path(
        "detail-req-drv-sch/<int:pk>/<slug:slug>/",
        DetailRequestDrivingSch.as_view(),
        name="detail-req-drv-sch",
    ),
    path(
        "delete-req-drv-sch/<int:pk>/<slug:slug>/",
        DeleteRequestDrivingSch.as_view(),
        name="delete-req-drv-sch",
    ),
    #  Driving Student Listing Search
    path(
        "search-approved-req-drv-sch/",
        SearchApprovedRequestDrivingSch.as_view(),
        name="search-approved-req-drv-sch",
    ),
    path(
        "search-unapproved-req-drv-sch/",
        SearchUnApprovedRequestDrivingSch.as_view(),
        name="search-unapproved-req-drv-sch",
    ),
    #  Listing car rental
    path(
        "list-approved-car-rental/",
        ListingCarRentalApproved.as_view(),
        name="list-approved-car-rental",
    ),
    path(
        "list-unapproved-car-rental/",
        ListingCarRentalUnApproved.as_view(),
        name="list-unapproved-car-rental",
    ),
    path(
        "detail-list-car-rental/<int:pk>/<slug:slug>/",
        DetailListingCarRental.as_view(),
        name="detail-list-car-rental",
    ),
    path(
        "delete-list-car-rental/<int:pk>/<slug:slug>/",
        DeleteListingCarRental.as_view(),
        name="delete-list-car-rental",
    ),
    #  Listing car rental search
    path(
        "search-list-approved-car-rental/",
        SearchApprovedListingCarRental.as_view(),
        name="search-list-approved-car-rental",
    ),
    path(
        "search-list-unapproved-car-rental/",
        SearchUnApprovedListingCarRental.as_view(),
        name="search-list-unapproved-car-rental",
    ),
]
