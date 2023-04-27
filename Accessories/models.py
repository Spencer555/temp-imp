from django.db import models
from django.utils.text import slugify
from custom.custom_func import unique_slugify
from Authentication.models import User
from django.core.validators import RegexValidator
import os 
from datetime import datetime
 

def accessories_path(instance, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join('accessories', timestamp, filename)

def accessories_images_path(instance, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join('accessories_images', timestamp, filename)


# Create your models here.
class Accessories(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    main_image = models.ImageField(upload_to=accessories_path)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(blank=True, null=True, editable=False)
    
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{1,3}?\s?\-?[0-9]{1,15}$',
        message="Phone number must be entered in the format: '+999 999999999'. Up to 15 digits allowed."
    )
    contact_no = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Accessories"

    def __str__(self):
        return f'{self.name}'
    
    

    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.name))
        super().save(*args, **kwargs)
        
        



class AccessoriesImages(models.Model):
    accessories =  models.ForeignKey(Accessories, related_name='accesory_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=accessories_images_path)
    slug = models.SlugField(blank=True, null=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.accessories.name}'
    
    class Meta:
        verbose_name_plural = "Accessory Images"

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.accessories.name))
        super().save(*args, **kwargs)

class AccessoriesEnquiry(models.Model):
    accessory =  models.ForeignKey(Accessories, related_name='accessory_enquiry', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{1,3}?\s?\-?[0-9]{1,15}$',
        message="Phone number must be entered in the format: '+999 999999999'. Up to 15 digits allowed."
    )
    contact_no = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True) 
    message = models.TextField()
    slug = models.SlugField(blank=True, null=True, editable=False)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    attended_to = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Accessory Enquires"

    def __str__(self):
        return f'{self.name}'
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.accessory.name))
        super().save(*args, **kwargs)


