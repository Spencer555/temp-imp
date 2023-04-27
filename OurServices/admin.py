from django.contrib import admin
from OurServices.models import ShipCarForUsSell, LetUsSellYourCar, ContactUsForEnquires,  CarRental, CarRentalImage, RentCar, RequestDrivingSch, ListCarRental, ListAccessories, ListDrivingSch
# Register your models here.
admin.site.register([ShipCarForUsSell, LetUsSellYourCar, ContactUsForEnquires,  CarRentalImage, CarRental, RentCar, RequestDrivingSch, ListCarRental, ListAccessories, ListDrivingSch])