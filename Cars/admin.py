from django.contrib import admin
from Cars.models import Car, CarEnquiry, CarImage
# Register your models here.


admin.site.register([CarImage, Car, CarEnquiry])