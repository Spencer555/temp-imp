from django.contrib import admin
from Accessories.models import (AccessoriesEnquiry, Accessories, AccessoriesImages)
# Register your models here.


admin.site.register([AccessoriesImages, Accessories, AccessoriesEnquiry])