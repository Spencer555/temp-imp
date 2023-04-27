from django.db import models
 
# Create your models here.

class Analytics(models.Model):
    ipaddress = models.CharField(max_length=100)
    time_visited = models.DateTimeField(auto_now_add=True)
    date_visited = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    times_views = models.PositiveIntegerField(default=0)
    device_family = models.CharField(max_length=200, blank=True, null=True)
    device_brand = models.CharField(max_length=200, blank=True, null=True)
    device_model = models.CharField(max_length=200, blank=True, null=True)
    browser_family = models.CharField(max_length=200, blank=True, null=True)
    browser_version = models.CharField(max_length=200, blank=True, null=True)
    browser_version_string = models.CharField(max_length=200, blank=True, null=True)
    os_family = models.CharField(max_length=200, blank=True, null=True)
    os_version = models.CharField(max_length=200, blank=True, null=True)
    os_version_string = models.CharField(max_length=200, blank=True, null=True)
    is_mobile = models.BooleanField(default=False)
    is_tablet = models.BooleanField(default=False)
    is_touch_capable = models.BooleanField(default=False)
    is_pc = models.BooleanField(default=False)
    is_bot = models.BooleanField(default=False)
    user = models.CharField(max_length=200, null=True, blank=True)

    
    class Meta:
        verbose_name_plural =  'Analytics'
    
    
    def __str__(self):
        return f'{self.ipaddress} - {self.times_views}'
    
    
    
    
    
    
    
    
    
     