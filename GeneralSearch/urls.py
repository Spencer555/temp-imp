from django.urls import path
from GeneralSearch.views import (
    # car search
    CarSearch,
    # accessory search
    AccessoriesSearch,
    # car rental search
    RentalCarsSearch,
)


urlpatterns = [
        # car search
    path("search-cars/", CarSearch.as_view(), name="search-cars"),
        # accessory search
    path("search-rentals/", RentalCarsSearch.as_view(), name="search-rentals"),
        # car rental search
    path("search-accessories/", AccessoriesSearch.as_view(), name="search-accessories"),
]
