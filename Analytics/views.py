from Analytics.models import Analytics
from Cars.models import Car, CarEnquiry
from Accessories.models import Accessories, AccessoriesEnquiry
from OurServices.models import CarRental, ShipCarForUsSell, LetUsSellYourCar, RentCar, ContactUsForEnquires
from datetime import datetime, timedelta, date
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic import (
    ListView,
) 
from django.contrib import messages
from django.db.models import Q
from OurServices.models import ListAccessories, ListCarRental, ListDrivingSch, RequestDrivingSch


# get client ip 
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
  



         
        
        
# get client data analytics
def ourAnalytics(data):
    
    op = get_client_ip(data)
    ipAdd = Analytics.objects.filter(ipaddress=op, date_visited=date.today())

    is_mobile = data.user_agent.is_mobile 
    is_tablet =  data.user_agent.is_tablet 
    is_touch = data.user_agent.is_touch_capable 
    is_pc =  data.user_agent.is_pc 
    is_bot =  data.user_agent.is_bot 

    browser_fam = data.user_agent.browser.family  
    browser_ver = data.user_agent.browser.version   
    browser_ver_str = data.user_agent.browser.version_string   

    os_family = data.user_agent.os.family  
    os_ver = data.user_agent.os.version  
    os_ver_str = data.user_agent.os.version_string  

    device_family  = data.user_agent.device.family  
    device_brand  = data.user_agent.device.brand  
    device_model  = data.user_agent.device.model  
    user = data.user.username
    

    if ipAdd.exists():
        ip = ipAdd.first()
        if datetime.now().astimezone() >= ip.time_visited + timedelta(hours=1):
            ip.times_views += 1
            ip.time_visited = datetime.now()
            ip.save()
    else:
        if user:
            ipAdd = Analytics.objects.create(ipaddress=op,views=1, times_views=1, is_mobile=is_mobile, is_tablet=is_tablet, is_touch_capable=is_touch, is_pc=is_pc, is_bot=is_bot, device_brand=device_brand, device_family=device_family, device_model=device_model, os_family= os_family, os_version=os_ver, os_version_string=os_ver_str, browser_family=browser_fam, browser_version=browser_ver, browser_version_string=browser_ver_str, user=user).save()
        else:
            ipAdd = Analytics.objects.create(ipaddress=op,views=1, times_views=1, is_mobile=is_mobile, is_tablet=is_tablet, is_touch_capable=is_touch, is_pc=is_pc, is_bot=is_bot, device_brand=device_brand, device_family=device_family, device_model=device_model, os_family= os_family, os_version=os_ver, os_version_string=os_ver_str, browser_family=browser_fam, browser_version=browser_ver, browser_version_string=browser_ver_str).save()
        if ipAdd:
            ipAdd.views += 1
            ipAdd.times_viewed += 1
            ipAdd.save()
        
    return HttpResponse(status=204)


# display main analytics

class MainAnalytics(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = Analytics
    context_object_name = 'analytics'
    template_name = 'analytics/analytics.html'
    paginate_by = 50 

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-time_visited')
        
        return queryset

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['ipData'] = Analytics.objects.all().order_by('-time_visited')
        context['cars'] = Car.objects.all().count()
        context['total_visits'] = Analytics.objects.all().count()
        context['total_pcs'] = Analytics.objects.filter(is_pc=True).count()
        context['total_mobile'] = Analytics.objects.filter(is_mobile=True).count()
        context['total_tabs'] = Analytics.objects.filter(is_tablet=True).count()
        context['total_bots'] = Analytics.objects.filter(is_bot=True).count()
        context['accessories'] = Accessories.objects.all().count()
        context['rentals'] = CarRental.objects.all().count()
        context['accessory_enquriy_attended'] = AccessoriesEnquiry.objects.filter(attended_to=True).count()
        context['accessory_enquriy_not_attended'] = AccessoriesEnquiry.objects.filter(attended_to=False).count()
        context['car_enquriy_attended'] = CarEnquiry.objects.filter(attended_to=True).count()
        context['car_enquriy_not_attended'] = CarEnquiry.objects.filter(attended_to=False).count()
        context['rent_car_attended'] = RentCar.objects.filter(attended_to=True).count()
        context['rent_car_not_attended'] = RentCar.objects.filter(attended_to=False).count()
        context['contact_enquriy_attended'] = ContactUsForEnquires.objects.filter(attended_to=True).count()
        context['contact_enquriy_not_attended'] = ContactUsForEnquires.objects.filter(attended_to=False).count()
        context['ship_enquriy_attended'] = ShipCarForUsSell.objects.filter(attended_to=True).count()
        context['ship_enquriy_not_attended'] = ShipCarForUsSell.objects.filter(attended_to=False).count()
        context['letus_enquriy_attended'] = LetUsSellYourCar.objects.filter(attended_to=True).count()
        context['letus_enquriy_not_attended'] = LetUsSellYourCar.objects.filter(attended_to=False).count()
        context['req_driving_attended'] = LetUsSellYourCar.objects.filter(attended_to=True).count()
        context['req_driving_not_attended'] = LetUsSellYourCar.objects.filter(attended_to=False).count()
        context['req_drisch_approved'] = RequestDrivingSch.objects.filter(approved=True).count()
        context['req_drisch_not_approved'] = RequestDrivingSch.objects.filter(approved=False).count()

        context['list_drisch_approved'] = ListDrivingSch.objects.filter(approved=True).count()
        context['list_drisch_not_approved'] = ListDrivingSch.objects.filter(approved=False).count()

        context['list_acc_approved'] = ListAccessories.objects.filter(approved=True).count()
        context['list_acc_not_approved'] = ListAccessories.objects.filter(approved=False).count()

        context['list_carRental_approved'] = ListCarRental.objects.filter(approved=True).count()
        context['list_carRental_not_approved'] = ListCarRental.objects.filter(approved=False).count()
        


        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

 



  
# search analytics
class AnalyticsSearch(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model =  Analytics
    context_object_name = 'analytics'
    template_name = 'analytics/search_analytics.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = Analytics.objects.filter(Q(ipaddress__icontains=query)) | Analytics.objects.filter(Q(time_visited__icontains=query)) | Analytics.objects.filter(Q(date_visited__icontains=query)) |  Analytics.objects.filter(Q(times_views__icontains=query)) |Analytics.objects.filter(Q(device_family__icontains=query)) | Analytics.objects.filter(Q(device_brand__icontains=query)) |Analytics.objects.filter(Q(device_model__icontains=query)) | Analytics.objects.filter(Q(browser_family__icontains=query)) | Analytics.objects.filter(Q(browser_version__icontains=query)) | Analytics.objects.filter(Q(browser_version_string__icontains=query)) | Analytics.objects.filter(Q(os_family__icontains=query)) | Analytics.objects.filter(Q(os_version__icontains=query)) |Analytics.objects.filter(Q(os_version_string__icontains=query)) | Analytics.objects.filter(Q(is_mobile__icontains=query)) | Analytics.objects.filter(Q(is_tablet__icontains=query)) | Analytics.objects.filter(Q(is_touch_capable__icontains=query)) | Analytics.objects.filter(Q(is_pc__icontains=query)) | Analytics.objects.filter(Q(is_bot__icontains=query)) | Analytics.objects.filter(Q(user__icontains=query))
            
        return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        context['ipData'] = Analytics.objects.all().order_by('-time_visited')
        context['cars'] = Car.objects.all().count()
        context['total_visits'] = Analytics.objects.all().count()
        context['total_pcs'] = Analytics.objects.filter(is_pc=True).count()
        context['total_mobile'] = Analytics.objects.filter(is_mobile=True).count()
        context['total_tabs'] = Analytics.objects.filter(is_tablet=True).count()
        context['total_bots'] = Analytics.objects.filter(is_bot=True).count()
        context['accessories'] = Accessories.objects.all().count()
        context['rentals'] = CarRental.objects.all().count()
        context['accessory_enquriy_attended'] = AccessoriesEnquiry.objects.filter(attended_to=True).count()
        context['accessory_enquriy_not_attended'] = AccessoriesEnquiry.objects.filter(attended_to=False).count()
        context['car_enquriy_attended'] = CarEnquiry.objects.filter(attended_to=True).count()
        context['car_enquriy_not_attended'] = CarEnquiry.objects.filter(attended_to=False).count()
        context['rent_car_attended'] = RentCar.objects.filter(attended_to=True).count()
        context['rent_car_not_attended'] = RentCar.objects.filter(attended_to=False).count()
        context['contact_enquriy_attended'] = ContactUsForEnquires.objects.filter(attended_to=True).count()
        context['contact_enquriy_not_attended'] = ContactUsForEnquires.objects.filter(attended_to=False).count()
        context['ship_enquriy_attended'] = ShipCarForUsSell.objects.filter(attended_to=True).count()
        context['ship_enquriy_not_attended'] = ShipCarForUsSell.objects.filter(attended_to=False).count()
        context['letus_enquriy_attended'] = LetUsSellYourCar.objects.filter(attended_to=True).count()
        context['letus_enquriy_not_attended'] = LetUsSellYourCar.objects.filter(attended_to=False).count()
        

        context['req_drisch_approved'] = RequestDrivingSch.objects.filter(approved=True).count()
        context['req_drisch_not_approved'] = RequestDrivingSch.objects.filter(approved=False).count()

        context['list_drisch_approved'] = ListDrivingSch.objects.filter(approved=True).count()
        context['list_drisch_not_approved'] = ListDrivingSch.objects.filter(approved=False).count()

        context['list_acc_approved'] = ListAccessories.objects.filter(approved=True).count()
        context['list_acc_not_approved'] = ListAccessories.objects.filter(approved=False).count()

        context['list_carRental_approved'] = ListCarRental.objects.filter(approved=True).count()
        context['list_carRental_not_approved'] = ListCarRental.objects.filter(approved=False).count()
        

        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

                 
        
        
         