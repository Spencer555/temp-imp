from django.shortcuts import render
from OurServices.models import ContactUsForEnquires, LetUsSellYourCar, ShipCarForUsSell, CarRental, CarRentalImage, RentCar, ListDrivingSch, ListAccessories, ListCarRental, RequestDrivingSch
 

from OurServices.forms import ContactUsForEnquiresForm, LetUsSellYourCarForm, ShipCarForUsSellForm, CarRentalForm, CarRentalImageForm, RentCarForm, ListAccessoriesForm, ListCarRentalForm, ReqDrvSchForm, ListDrivingSchForm 


from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    View
)
from django.db.models import Q

# Create your views here.
# create update delete list detail


# contact us for enquires 
class CreateContactUsForEnquires(CreateView):
    model = ContactUsForEnquires
    form_class = ContactUsForEnquiresForm 
    context_object_name = 'contact_us'
    template_name = 'our_services/contact_enquiry/contact_enquiry_create.html'
    
    def form_valid(self, form):
        return super().form_valid(form)

 
    def get_success_url(self):
        messages.success(self.request, 'Enquiry Sent')
        return reverse('services-home')       




class DetailContactUsForEnquires(UserPassesTestMixin,  LoginRequiredMixin, DetailView):
    model = ContactUsForEnquires
    form_class = ContactUsForEnquiresForm 
    context_object_name = 'contact_us'
    template_name = 'our_services/contact_enquiry/detail_contact_enquiry.html'
    
    # attended to and unattend to
    def post(self, request, *args, **kwargs):
        user = request.user
        contact_us = self.get_object()
        if user.is_staff or user.is_superuser:
            contact_us.attended_to = not contact_us.attended_to 
            contact_us.save()
            if contact_us.attended_to == False:
                messages.success(request, 'Unattended To')
            else:
                messages.success(request, 'Attended To')
            return redirect(self.request.path_info)
        
        messages.error(request, 'Error, Try Again!')
        return redirect(self.request.path_info)

 
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

 

class DeleteContactUsForEnquires(UserPassesTestMixin, DeleteView, LoginRequiredMixin):
    model = ContactUsForEnquires
    form_class = ContactUsForEnquiresForm 
    context_object_name = 'contact_us'
    template_name = 'our_services/contact_enquiry/contact_enquiry_delete.html'
    
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser :
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
            
    def get_success_url(self):
        messages.success(self.request, "Contact Enquiry Deleted")
        return reverse('list-contact-enquiry-attended-to')



class ListContactUsForEnquiresAttended(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = ContactUsForEnquires
    context_object_name = 'contact_us'
    template_name = 'our_services/contact_enquiry/contact_enquiry_list_attended_to.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(attended_to=True).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False


class ListContactUsForEnquiresNotAttended(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = ContactUsForEnquires
    context_object_name = 'contact_us'
    template_name = 'our_services/contact_enquiry/contact_enquiry_list_not_attended_to.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(attended_to=False).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False




# contact enq search
class ContactEnquiryNotAttendedToEnquirySearch(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    
    model =  ContactUsForEnquires
    context_object_name = 'contact_us'
    template_name = 'our_services/contact_enquiry/search_contact_enquiry_not_attended_to.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = ContactUsForEnquires.objects.filter(Q(name__icontains=query), attended_to=False)  |  ContactUsForEnquires.objects.filter(Q(contact__icontains=query), attended_to=False)  |  ContactUsForEnquires.objects.filter(Q(enquiry__icontains=query), attended_to=False)  |  ContactUsForEnquires.objects.filter(Q(email__icontains=query), attended_to=False)  
                    
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

       
     
class ContactEnquiryAttendedToEnquirySearch(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    
    model =  ContactUsForEnquires
    context_object_name = 'contact_us'
    template_name = 'our_services/contact_enquiry/search_contact_enquiry_attended_to.html'
    paginate_by = 50 

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = ContactUsForEnquires.objects.filter(Q(name__icontains=query), attended_to=True)  |  ContactUsForEnquires.objects.filter(Q(contact__icontains=query), attended_to=True)  |  ContactUsForEnquires.objects.filter(Q(enquiry__icontains=query), attended_to=True)  |  ContactUsForEnquires.objects.filter(Q(email__icontains=query), attended_to=True)  
            
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

       
     
 

# letussellyourcar
class CreateLetUsSellYourCar(CreateView, UserPassesTestMixin):
    model = LetUsSellYourCar
    form_class = LetUsSellYourCarForm
    context_object_name = 'sell_your_car'
    template_name = 'our_services/sell_your_car/sell_your_car_create.html'
    
    def test_func(self):
        user = self.request.user          
        if self.request.method == 'POST':
            messages.success(self.request, 'Sent. Thank You!')
            return True
        return True



class DetailLetUsSellYourCar(UserPassesTestMixin,  LoginRequiredMixin, DetailView):
    model = LetUsSellYourCar
    context_object_name = 'sell_your_car'
    template_name = 'our_services/sell_your_car/detail_sell_your_car.html'

# attended to an unattend to

    def post(self, request, *args, **kwargs):
        user = request.user
        sell_ur_car = self.get_object()
        if user.is_staff or user.is_superuser:
            sell_ur_car.attended_to = not sell_ur_car.attended_to 
            sell_ur_car.save()
            if sell_ur_car.attended_to == False:
                messages.success(request, 'Unattended To')
            else:
                messages.success(request, 'Attended To')
            return redirect(self.request.path_info)
        
        messages.error(request, 'Error, Try Again!')
        return redirect(self.request.path_info)
    
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False






class DeleteLetUsSellYourCar(UserPassesTestMixin,  LoginRequiredMixin, DeleteView):
    model = LetUsSellYourCar
    context_object_name = 'sell_your_car'
    template_name = 'our_services/sell_your_car/delete_sell_your_car.html'

    def get_success_url(self):
        messages.success(self.request, 'Car Sale Request Deleted')
        return reverse('sell-your-car-attended-to')

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser :
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')

        return False
 


class ListLetUsSellYourCarAttendedTo(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = LetUsSellYourCar
    context_object_name = 'sell_your_car'
    template_name = 'our_services/sell_your_car/list_sell_your_car_attended_to.html'
    paginate_by = 50
    

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(attended_to=True).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
  
class ListLetUsSellYourCarNotAttendedTo(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = LetUsSellYourCar
    context_object_name = 'sell_your_car'
    template_name = 'our_services/sell_your_car/list_sell_your_car_not_attended_to.html'
    paginate_by = 50
    

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(attended_to=False).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
  
# search let us sell ur car
class LetUsSellYourCarSearchNotAttendedTo(UserPassesTestMixin,  ListView, LoginRequiredMixin):  
    model =  LetUsSellYourCar
    context_object_name = 'sell_your_car'
    template_name = 'our_services/sell_your_car/search_sell_your_car_not_attended_to.html'
    paginate_by = 50
    
 
 
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:                 
            queryset = LetUsSellYourCar.objects.filter(Q(contact__icontains=query), attended_to=False)  | LetUsSellYourCar.objects.filter(Q(your_name__icontains=query), attended_to=False)  | LetUsSellYourCar.objects.filter(Q(description__icontains=query), attended_to=False)  | LetUsSellYourCar.objects.filter(Q(title__icontains=query), attended_to=False)  |  LetUsSellYourCar.objects.filter(Q(condition__icontains=query), attended_to=False)     |   LetUsSellYourCar.objects.filter(Q(mileage__icontains=query), attended_to=False)  | LetUsSellYourCar.objects.filter(Q(location__icontains=query), attended_to=False)  |  LetUsSellYourCar.objects.filter(Q(region__icontains=query), attended_to=False)  | LetUsSellYourCar.objects.filter(Q(price__icontains=query), attended_to=False)  |  LetUsSellYourCar.objects.filter(Q(email__icontains=query), attended_to=False)  | LetUsSellYourCar.objects.filter(Q(accessories__icontains=query), attended_to=False)  |  LetUsSellYourCar.objects.filter(Q(makes_and_model__icontains=query), attended_to=False)  |   LetUsSellYourCar.objects.filter(Q(interior_color__icontains=query), attended_to=False)  |    LetUsSellYourCar.objects.filter(Q(color__icontains=query), attended_to=False)  |   LetUsSellYourCar.objects.filter(Q(year_manufactured__icontains=query), attended_to=False)  |   LetUsSellYourCar.objects.filter(Q(transmission__icontains=query), attended_to=False)  |    LetUsSellYourCar.objects.filter(Q(fuel__icontains=query), attended_to=False)  |  LetUsSellYourCar.objects.filter(Q(steering__icontains=query), attended_to=False)   
                    
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
  
  

class LetUsSellYourCarSearchAttendedTo(UserPassesTestMixin, LoginRequiredMixin, ListView):  
    model =  LetUsSellYourCar
    context_object_name = 'sell_your_car'
    template_name = 'our_services/sell_your_car/search_sell_your_car_attended_to.html'
    paginate_by = 50 
    
  
 
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:                 
            queryset = LetUsSellYourCar.objects.filter(Q(contact__icontains=query), attended_to=True)  | LetUsSellYourCar.objects.filter(Q(your_name__icontains=query), attended_to=True)  | LetUsSellYourCar.objects.filter(Q(description__icontains=query), attended_to=True)  | LetUsSellYourCar.objects.filter(Q(title__icontains=query), attended_to=True)  |  LetUsSellYourCar.objects.filter(Q(condition__icontains=query), attended_to=True)     |   LetUsSellYourCar.objects.filter(Q(mileage__icontains=query), attended_to=True)  | LetUsSellYourCar.objects.filter(Q(location__icontains=query), attended_to=True)  |  LetUsSellYourCar.objects.filter(Q(region__icontains=query), attended_to=True)  | LetUsSellYourCar.objects.filter(Q(price__icontains=query), attended_to=True)  |  LetUsSellYourCar.objects.filter(Q(email__icontains=query), attended_to=True)  | LetUsSellYourCar.objects.filter(Q(accessories__icontains=query), attended_to=True)  |  LetUsSellYourCar.objects.filter(Q(makes_and_model__icontains=query), attended_to=True)  |   LetUsSellYourCar.objects.filter(Q(interior_color__icontains=query), attended_to=True)  |    LetUsSellYourCar.objects.filter(Q(color__icontains=query), attended_to=True)  |   LetUsSellYourCar.objects.filter(Q(year_manufactured__icontains=query), attended_to=True)  |   LetUsSellYourCar.objects.filter(Q(transmission__icontains=query), attended_to=True)  |    LetUsSellYourCar.objects.filter(Q(fuel__icontains=query), attended_to=True)  |  LetUsSellYourCar.objects.filter(Q(steering__icontains=query), attended_to=True)  
                    
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

    
           
         
     
 


# shipcarforustosell 

class CreateShipCarForUsSell(CreateView, UserPassesTestMixin):
    model = ShipCarForUsSell
    form_class = ShipCarForUsSellForm
    context_object_name = 'ship_car_to_sell'
    template_name = 'our_services/ship_car_to_sell/ship_car_to_sell_create.html'
    
    def test_func(self):
        user = self.request.user 

        
        if self.request.method == 'POST':
            messages.success(self.request, 'Sent. Thank You!')
            return True
        return True



class DetailShipCarForUsSell(UserPassesTestMixin, DetailView, LoginRequiredMixin):
    model = ShipCarForUsSell
    context_object_name = 'ship_car_to_sell'
    template_name = 'our_services/ship_car_to_sell/detail_ship_car_to_sell.html'
    
#  attended to and unattend to    
    def post(self, request, *args, **kwargs):
        user = request.user
        ship_car = self.get_object()
        if user.is_staff or user.is_superuser:
            ship_car.attended_to = not ship_car.attended_to 
            ship_car.save()
            if ship_car.attended_to == False:
                messages.success(request, 'Unattended To')
            else:
                messages.success(request, 'Attended To')
            return redirect(self.request.path_info)
        
        messages.error(request, 'Error, Try Again!')
        return redirect(self.request.path_info)


    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False






class DeleteShipCarForUsSell(UserPassesTestMixin,  LoginRequiredMixin, DeleteView):
    model = ShipCarForUsSell
    context_object_name = 'ship_car_to_sell'
    template_name = 'our_services/ship_car_to_sell/delete_ship_car_to_sell.html'

    def get_success_url(self):
        messages.success(self.request, 'Ship Car Sale Request Deleted')
        return reverse('list-ship-car-attended-to')
 
    
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser :
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')

        return False
    
    
    




class ListShipCarForUsSellAttendedTo(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = ShipCarForUsSell
    context_object_name = 'ship_car_to_sell'
    template_name = 'our_services/ship_car_to_sell/list_ship_car_to_sell_attended_to.html'
    paginate_by = 50

    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(attended_to=True).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

  
class ListShipCarForUsSellNotAttendedTo(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = ShipCarForUsSell
    context_object_name = 'ship_car_to_sell'
    template_name = 'our_services/ship_car_to_sell/list_ship_car_to_sell_not_attended_to.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(attended_to=False).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
   

# search car ship for us to sell
class ShipCarForUsSellSearchNotAttendedTo(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    model =  ShipCarForUsSell
    context_object_name = 'ship_car_to_sell'
    template_name = 'our_services/ship_car_to_sell/search_list_ship_car_to_sell_not_attended_to.html'
    paginate_by = 50 
    
 
 
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:        
                     
            queryset = ShipCarForUsSell.objects.filter(Q(contact__icontains=query), attended_to=False)  | ShipCarForUsSell.objects.filter(Q(your_name__icontains=query), attended_to=False)  | ShipCarForUsSell.objects.filter(Q(description__icontains=query), attended_to=False)  | ShipCarForUsSell.objects.filter(Q(title__icontains=query), attended_to=False)  |  ShipCarForUsSell.objects.filter(Q(condition__icontains=query), attended_to=False)    |  ShipCarForUsSell.objects.filter(Q(mileage__icontains=query), attended_to=False)  | ShipCarForUsSell.objects.filter(Q(location__icontains=query), attended_to=False)  |  ShipCarForUsSell.objects.filter(Q(price__icontains=query), attended_to=False)  |  ShipCarForUsSell.objects.filter(Q(email__icontains=query), attended_to=False)  | ShipCarForUsSell.objects.filter(Q(accessories__icontains=query), attended_to=False)  | ShipCarForUsSell.objects.filter(Q(country__icontains=query), attended_to=False)  | ShipCarForUsSell.objects.filter(Q(makes_and_model__icontains=query), attended_to=False)  |  ShipCarForUsSell.objects.filter(Q(year_manufactured__icontains=query), attended_to=False)     | ShipCarForUsSell.objects.filter(Q(transmission__icontains=query), attended_to=False) | ShipCarForUsSell.objects.filter(Q(color__icontains=query), attended_to=False)    | ShipCarForUsSell.objects.filter(Q(steering__icontains=query), attended_to=False)  | ShipCarForUsSell.objects.filter(Q(interior_color__icontains=query))    | ShipCarForUsSell.objects.filter(Q(fuel__icontains=query), attended_to=False)  
                    
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
 
 
 
 
 
class ShipCarForUsSellSearchAttendedTo(UserPassesTestMixin, LoginRequiredMixin, ListView):     
    model =  ShipCarForUsSell
    context_object_name = 'ship_car_to_sell'
    template_name = 'our_services/ship_car_to_sell/search_list_ship_car_to_sell_attended_to.html'
    paginate_by = 50 
    
 
 
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:                 
            queryset = ShipCarForUsSell.objects.filter(Q(contact__icontains=query), attended_to=True)  | ShipCarForUsSell.objects.filter(Q(your_name__icontains=query), attended_to=True)  | ShipCarForUsSell.objects.filter(Q(description__icontains=query), attended_to=True)  | ShipCarForUsSell.objects.filter(Q(title__icontains=query), attended_to=True)  |  ShipCarForUsSell.objects.filter(Q(condition__icontains=query), attended_to=True)    |  ShipCarForUsSell.objects.filter(Q(mileage__icontains=query), attended_to=True)  | ShipCarForUsSell.objects.filter(Q(location__icontains=query), attended_to=True)  |  ShipCarForUsSell.objects.filter(Q(price__icontains=query), attended_to=True)  |  ShipCarForUsSell.objects.filter(Q(email__icontains=query), attended_to=True)  | ShipCarForUsSell.objects.filter(Q(accessories__icontains=query), attended_to=True)  | ShipCarForUsSell.objects.filter(Q(country__icontains=query), attended_to=True)  | ShipCarForUsSell.objects.filter(Q(makes_and_model__icontains=query), attended_to=True)  |  ShipCarForUsSell.objects.filter(Q(year_manufactured__icontains=query), attended_to=True)     | ShipCarForUsSell.objects.filter(Q(transmission__icontains=query), attended_to=True) | ShipCarForUsSell.objects.filter(Q(color__icontains=query), attended_to=True)    | ShipCarForUsSell.objects.filter(Q(steering__icontains=query), attended_to=True)  | ShipCarForUsSell.objects.filter(Q(interior_color__icontains=query))    | ShipCarForUsSell.objects.filter(Q(fuel__icontains=query), attended_to=True)  
                    
        return queryset


        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

     

# car rentals 

class CreateCarRentals(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CarRental
    form_class = CarRentalForm
    context_object_name = 'car_rental'
    template_name = 'our_services/car_rental/create_car_rental.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

 
    def get_success_url(self):
        messages.success(self.request, 'Car Rental Created')
        return reverse('create-car-rental')  
    
         

        
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')

        return False

# contains the forms for carrental, rental image, rent car,
class DetailCarRentals(DetailView):
    model = CarRental
    context_object_name = 'car_rental'
    template_name = 'our_services/car_rental/detail_car_rental.html'
    
    # gets car for rent its rental image and the rent car enquiry form
    def get(self, request, *args, **kwargs):
        car_for_rent = self.get_object()
        car_rental_image = CarRentalImage.objects.filter(car=car_for_rent)
        rent_car_form = RentCarForm()
        
        context = {
            'car_rental': car_for_rent,
            'car_rental_image':car_rental_image,
            'rent_car_form':rent_car_form
        }
        return render(request, self.template_name, context)
    
    
         
    def post(self, request, *args, **kwagrs):
        user = request.user
        
        # add image to rental
        if request.POST['type'] == 'rental_image':
            if user == user.is_staff or user.is_superuser :
                car_rental = self.get_object()
                request.POST._mutable = True
                request.POST['user'] = user 
                request.POST['car'] = car_rental
                request.FILES['image'] = request.FILES['image']
                request.POST._mutable = False

                car_rental_image_form = CarRentalImageForm(self.request.POST, self.request.FILES)
                
                if car_rental_image_form.is_valid():
                    car_rental_image_form.save()
                    messages.success(request, 'Image Added')
                    return redirect(self.request.path_info)
                messages.warning(request, 'Image Not Added Try Again!')
                return redirect(self.request.path_info)
            
            messages.warning(request, 'Image Not Added Try Again!')
            return redirect(self.request.path_info)

        #  make a enquiry to rent car
        elif request.POST['type'] == 'rent_enquiry':
            car = self.get_object()
            request.POST._mutable = True
            request.POST['car'] = car
            request.POST._mutable = False
             
            

            rent_car_enquiry_form = RentCarForm(request.POST)
            if  rent_car_enquiry_form.is_valid():
                rent_car_enquiry_form.save()
                messages.success(request, 'Enquiry Sent')
                return redirect(self.request.path_info)
            else:
                if 'contact' in rent_car_enquiry_form.errors:
                    error = rent_car_enquiry_form.errors['contact'][0]
                    messages.warning(request, f'Not Sent!  {error}')
                    return redirect(self.request.path_info)
    
                else:
                    messages.warning(request, 'Error! Enquiry Not Sent')
                    return redirect(self.request.path_info)

                    
                     
      
    #    delete car rental image
        elif request.POST['type'] == 'delete':
            id = request.POST['id'] 
            slug = request.POST['slug'] 
            
            image =  CarRentalImage.objects.filter(id=id, slug=slug).first()
            
            
            if image:
                image.delete()
                messages.success(request, 'Image Deleted')
                return redirect(self.request.path_info)
            else:
                messages.warning(request, 'Not Deleted! Pls Try Again')
                return redirect(self.request.path_info)

      
      
       
       
        messages.warning(request, 'Error Please Try Again')
        return redirect(self.request.path_info)

        
       

class ListCarRentals(ListView):
    model = CarRental
    context_object_name = 'car_rental'
    template_name = 'our_services/car_rental/list_car_rental.html'
    queryset = CarRental.objects.all().order_by('-created')
    paginate_by = 50

class UpdatCarRentals(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = CarRental
    form_class = CarRentalForm
    context_object_name = 'car_rental'
    template_name = 'our_services/car_rental/update_car_rental.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

 
    def get_success_url(self):
        messages.success(self.request, 'Car Rental Updated')
        return reverse('detail-car-rental', kwargs={'slug':self.get_object().slug, 'pk':self.get_object().id})       

    
    def test_func(self):
        user = self.request.user 
        car_rental = self.get_object()
        if user.is_staff or user.is_superuser or car_rental.user:
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')

        return False


class DeleteCarRentals(UserPassesTestMixin,  LoginRequiredMixin, DeleteView):
    model = CarRental
    context_object_name = 'car_rental'
    template_name = 'our_services/car_rental/car_rental_delete.html'

    def test_func(self):
        user = self.request.user 
        car_rental = self.get_object()
        if user.is_staff or user.is_superuser or car_rental.user:
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')

        return False
        
    def get_success_url(self):
        messages.success(self.request, 'Car Rental Deleted')
        return reverse('list-car-rental')





# Rent Car enquires
class ListRentCarNotAttendedTo(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = RentCar
    context_object_name = 'rent_car'
    template_name = 'our_services/car_rental/rent_car/list_car_rent_not_attended_to.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(attended_to=False).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
  

class ListRentCarAttendedTo(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = RentCar
    context_object_name = 'rent_car'
    template_name = 'our_services/car_rental/rent_car/list_car_rent_attended_to.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(attended_to=True).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
  


class DeleteRentCar(UserPassesTestMixin,  LoginRequiredMixin, DeleteView):
    model = RentCar
    context_object_name = 'rent_car'
    template_name = 'our_services/car_rental/rent_car/delete_rent_car.html'

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser :
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')

        return False
    
    def get_success_url(self):
        messages.success(self.request, 'Deleted Succesfully')

        return reverse('list-car-rent-enquiry-not-attended-to')


class DetailRentCar(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = RentCar
    form_class = RentCarForm
    context_object_name = 'rent_car'
    template_name = 'our_services/car_rental/rent_car/detail_car_rent.html'
    
    # attend to and unattend to 
    def post(self, request, *args, **kwargs):
        user = request.user
        rent_car = self.get_object()
        if user.is_staff or user.is_superuser:
            rent_car.attended_to = not rent_car.attended_to 
            rent_car.save()
            if rent_car.attended_to == False:
                messages.success(request, 'Unattended To')
            else:
                messages.success(request, 'Attended To')
            return redirect(self.request.path_info)
        
        messages.error(request, 'Error, Try Again!')
        return redirect(self.request.path_info)
    
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False


    
    

    
    


        
    
  
 
# contains contact form, sell ur car form, ship car form , request driving sch form, list car rental form, list driving sch form, list accessories form
class ServicesHome(View):
    
    template_name = 'our_services/services_home.html'
    contact_form = ContactUsForEnquiresForm()
    sell_your_car_form = LetUsSellYourCarForm()
    ship_car_form = ShipCarForUsSellForm()
    list_car_rental_form = ListCarRentalForm()
    request_drv_sch_form = ReqDrvSchForm()
    list_drv_sch_form = ListDrivingSchForm()
    list_accessessories_form = ListAccessoriesForm()
    
        
    context = {
        'contact_form':contact_form,
        'sell_your_car_form':sell_your_car_form,
        'ship_car_form': ship_car_form,
        'req_drv_sch_form': request_drv_sch_form,
        'list_car_rental_form': list_car_rental_form,
        'list_drv_sch_form': list_drv_sch_form,
        'list_accessories_form': list_accessessories_form,
        
    }
    
    
    def get(self, request):     
        
        return render(request,  'our_services/services_home.html', self.context)
    
    def post(self, request, *args, **kwargs):
       
        # submit contact enquiry form
        if request.POST['type'] == 'contact_enquiry':
            contact_form = ContactUsForEnquiresForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, 'Contact Enquiry Sent')
                self.context['contact_form'] = self.contact_form

                return redirect(self.request.path_info)
            else:
                # Pass the form instance with errors to the template context
                self.context['contact_form'] = contact_form
                messages.warning(request, 'Contact Enquiry Not Sent. Please fix the errors below.')
                return render(request, self.template_name, self.context)
             
        # submit sell ur car form
        elif request.POST['type'] == 'sell_your_car':
            sell_your_car_form = LetUsSellYourCarForm(request.POST, request.FILES)
            if sell_your_car_form.is_valid():
                sell_your_car_form.save()
                messages.success(request, 'Sell Car Request Sent')
                self.context['sell_your_car_form'] = self.sell_your_car_form

                return redirect(self.request.path_info)
            else:
                # Pass the form instance with errors to the template context

                self.context['sell_your_car_form'] = sell_your_car_form
                messages.warning(request, 'Sell Car Request Not Sent Try Again!')
                return render(request, self.template_name, self.context)
        
        #submit request driving sch form
        elif request.POST['type'] == 'request_drv_sch':
            request_drv_sch_form = ReqDrvSchForm(request.POST)
            if request_drv_sch_form.is_valid():
                request_drv_sch_form.save()
                messages.success(request, 'Request Sent')
                self.context['req_drv_sch_form'] =  self.request_drv_sch_form

                return redirect(self.request.path_info)
            else:
                # Pass the form instance with errors to the template context

                self.context['req_drv_sch_form'] =  request_drv_sch_form
                messages.warning(request, 'Request Not Sent Try Again!')
                return render(request, self.template_name, self.context)
        
        # submit request Listing car rental form
        elif request.POST['type'] == 'list_car_rental':
            list_car_rental_form = ListCarRentalForm(request.POST, request.FILES)
            if list_car_rental_form.is_valid():
                list_car_rental_form.save()
                messages.success(request, 'Request Sent')
                self.context['list_car_rental_form'] = self.list_car_rental_form

                return redirect(self.request.path_info)
            
            else:
                # Pass the form instance with errors to the template context
                
                self.context['list_car_rental_form'] = list_car_rental_form
                messages.warning(request, 'Request Not Sent Try Again!')
                return render(request, self.template_name, self.context)
        
        # submit listing driving sch form
        elif request.POST['type'] == 'list_drv_sch':
            list_drv_sch_form = ListDrivingSchForm(request.POST)
            if list_drv_sch_form.is_valid():
                list_drv_sch_form.save()
                messages.success(request, 'Request Sent')
                self.context['list_drv_sch_form'] = self.list_drv_sch_form

                return redirect(self.request.path_info)
            else:
                # Pass the form instance with errors to the template context

                self.context['list_drv_sch_form'] = list_drv_sch_form         
                messages.warning(request, 'Request Not Sent Try Again!')
                return render(request, self.template_name, self.context)
        
        #submit listing accessory form
        elif request.POST['type'] == 'list_accessory':
            list_acc_form = ListAccessoriesForm(request.POST, request.FILES)
            if list_acc_form.is_valid():
                list_acc_form.save()
                messages.success(request, 'Request Sent')
                self.context['list_accessories_form'] = self.list_accessessories_form

                return redirect(self.request.path_info)
            else:
                # Pass the form instance with errors to the template context

                self.context['list_accessories_form'] = list_acc_form

                messages.warning(request, 'Request Not Sent Try Again!')
                return render(request, self.template_name, self.context)
        
        
    
        #sumbit listing ship your car form 
        elif request.POST['type'] == 'ship_your_car':
            ship_your_car_form = ShipCarForUsSellForm(request.POST, request.FILES)
            if ship_your_car_form.is_valid():
                ship_your_car_form.save()
                messages.success(request, 'Sell Car Request Sent')
                self.context['ship_car_form'] = self.ship_car_form

                return redirect(self.request.path_info)
            else:
                # Pass the form instance with errors to the template context

                self.context['ship_car_form'] = ship_your_car_form
                messages.warning(request, 'Sell Car Request Not Sent Try Again!')
                return render(request, self.template_name, self.context)
        
    
        else:
            messages.warning(request, 'Error Please Try Again')
            return redirect(self.request.path_info)


        
        # search rentcar 

class RentCarSearchAttendedTo(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    model =  RentCar
    context_object_name = 'rent_car'
    template_name = 'our_services/car_rental/rent_car/search_rent_cars_attended_to.html'
    paginate_by = 50 
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = RentCar.objects.filter(Q(name__icontains=query), attended_to=True)  | RentCar.objects.filter(Q(location__icontains=query), attended_to=True)  | RentCar.objects.filter(Q(contact__icontains=query), attended_to=True)  | RentCar.objects.filter(Q(email__icontains=query), attended_to=True)  |RentCar.objects.filter(Q(region__icontains=query), attended_to=True)  | RentCar.objects.filter(Q(car__car__icontains=query), attended_to=True)  
                    
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

    
class RentCarSearchNotAttendedTo(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    model =  RentCar
    context_object_name = 'rent_car'
    template_name = 'our_services/car_rental/rent_car/search_rent_cars_not_attended_to.html'
    paginate_by = 50 
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = RentCar.objects.filter(Q(name__icontains=query), attended_to=False)  | RentCar.objects.filter(Q(location__icontains=query), attended_to=False)  | RentCar.objects.filter(Q(contact__icontains=query), attended_to=False)  | RentCar.objects.filter(Q(email__icontains=query), attended_to=False)  |RentCar.objects.filter(Q(region__icontains=query), attended_to=False)  | RentCar.objects.filter(Q(car__car__icontains=query), attended_to=False)  
                    
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

    

# List your accessories
class CreateListAccessories(CreateView):
    model = ListAccessories
    form_class = ListAccessoriesForm
    context_object_name = 'list_acc'
    template_name = 'our_services/list_accessory/list_accessory_create.html'
    
    def form_valid(self, form):
        return super().form_valid(form)

 
    def get_success_url(self):
        messages.success(self.request, 'Enquiry Sent')
        return reverse('services-home')       



class DetailListAccessories(UserPassesTestMixin,  LoginRequiredMixin, DetailView):
    model = ListAccessories
    form_class = ListAccessoriesForm 
    context_object_name = 'list_acc'
    template_name = 'our_services/list_accessory/list_accessory_detail.html'
    
    # approve and unapprove
    def post(self, request, *args, **kwargs):
        user = request.user
        list_acc = self.get_object()
        if user.is_staff or user.is_superuser:
            list_acc.approved = not list_acc.approved 
            list_acc.save()
            if list_acc.approved == False:
                messages.success(request, 'UnApproved')
            else:
                messages.success(request, 'Approved')
            return redirect(self.request.path_info)
        
        messages.error(request, 'Error, Try Again!')
        return redirect(self.request.path_info)

 
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

 

class DeleteListAccessories(UserPassesTestMixin, DeleteView, LoginRequiredMixin):
    model = ListAccessories
    context_object_name = 'list_acc'
    template_name = 'our_services/list_accessory/list_accessory_delete.html'
    
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser :
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
            
    def get_success_url(self):
        messages.success(self.request, "Accessory Listing  Deleted")
        return reverse('list-approved-accessories')



class ListAccessoriesApproved(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = ListAccessories
    context_object_name = 'list_acc'
    template_name = 'our_services/list_accessory/list_accessory_approved.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(approved=True).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False


class ListAccessoriesUnApproved(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = ListAccessories
    context_object_name = 'list_acc'
    template_name = 'our_services/list_accessory/list_accessory_unapproved.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(approved=False).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False




# search accessories listing
class  SearchApprovedListAccessories(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    
    model =  ListAccessories
    context_object_name = 'list_acc'
    template_name = 'our_services/list_accessory/list_accessory_search_approved.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = ListAccessories.objects.filter(Q(name__icontains=query), approved=True)  |  ListAccessories.objects.filter(Q(contact_no__icontains=query), approved=True)  |  ListAccessories.objects.filter(Q(description__icontains=query), approved=True)  |  ListAccessories.objects.filter(Q(email__icontains=query), approved=True) |  ListAccessories.objects.filter(Q(region__icontains=query), approved=True)  |  ListAccessories.objects.filter(Q(price__icontains=query), approved=True)
              
                    
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

       
     
class SearchUnApprovedListAccessories(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    
    model =  ListAccessories
    context_object_name = 'list_acc'
    template_name = 'our_services/list_accessory/list_accessory_search_unapproved.html'
    paginate_by = 50 

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
           queryset = ListAccessories.objects.filter(Q(name__icontains=query), approved=False)  |  ListAccessories.objects.filter(Q(contact_no__icontains=query), approved=False)  |  ListAccessories.objects.filter(Q(description__icontains=query), approved=False)  |  ListAccessories.objects.filter(Q(email__icontains=query), approved=False) |  ListAccessories.objects.filter(Q(region__icontains=query), approved=False)  |  ListAccessories.objects.filter(Q(price__icontains=query), approved=False)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

       
     
#  list driving sch
 

class DetailListDrivingSch(UserPassesTestMixin,  LoginRequiredMixin, DetailView):
    model = ListDrivingSch
    form_class = ListDrivingSchForm 
    context_object_name = 'drv_sch'
    template_name = 'our_services/driving_sch/listing_drv_sch_detail.html'
    
    # contains approve or unapprove
    
    def post(self, request, *args, **kwargs):
        user = request.user
        drv_sch = self.get_object()
        if user.is_staff or user.is_superuser:
            drv_sch.approved = not drv_sch.approved 
            drv_sch.save()
            if drv_sch.approved == False:
                messages.success(request, 'UnApproved')
            else:
                messages.success(request, 'Approved')
            return redirect(self.request.path_info)
        
        messages.error(request, 'Error, Try Again!')
        return redirect(self.request.path_info)

 
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

 

class DeleteListDrivingSch(UserPassesTestMixin, DeleteView, LoginRequiredMixin):
    model = ListDrivingSch
    context_object_name = 'drv_sch'
    template_name = 'our_services/driving_sch/listing_drv_sch_delete.html'
    
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser :
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
            
    def get_success_url(self):
        messages.success(self.request, "Driving Request  Deleted")
        return reverse('list-approved-drv-sch')



class ListDrivingSchApproved(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = ListDrivingSch
    context_object_name = 'drv_sch'
    template_name = 'our_services/driving_sch/listing_drv_sch_approved.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(approved=True).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False


class ListDrivingSchUnApproved(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = ListDrivingSch
    context_object_name = 'drv_sch'
    template_name = 'our_services/driving_sch/listing_drv_sch_unapproved.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(approved=False).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False




# search list drv sch
class  SearchApprovedListDrivingSch(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    
    model =  ListDrivingSch
    context_object_name = 'drv_sch'
    template_name = 'our_services/driving_sch/listing_drv_sch_search_approved.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = ListDrivingSch.objects.filter(Q(name__icontains=query), approved=True)|  ListDrivingSch.objects.filter(Q(location__icontains=query), approved=True) |  ListDrivingSch.objects.filter(Q(driving_sch_name__icontains=query), approved=True)|  ListDrivingSch.objects.filter(Q(services_offered__icontains=query), approved=True)|  ListDrivingSch.objects.filter(Q(email__icontains=query), approved=True)|  ListDrivingSch.objects.filter(Q(contact_no__icontains=query), approved=True) |   ListDrivingSch.objects.filter(Q(region__icontains=query), approved=True)
                    
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

       
     
class SearchUnApprovedListDrivingSch(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    
    model =  ListDrivingSch
    context_object_name = 'drv_sch'
    template_name = 'our_services/driving_sch/listing_drv_sch_search_unapproved.html'
    paginate_by = 50 

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = ListDrivingSch.objects.filter(Q(name__icontains=query), approved=False)|  ListDrivingSch.objects.filter(Q(location__icontains=query), approved=False) |  ListDrivingSch.objects.filter(Q(driving_sch_name__icontains=query), approved=False)|  ListDrivingSch.objects.filter(Q(services_offered__icontains=query), approved=False)|  ListDrivingSch.objects.filter(Q(email__icontains=query), approved=False)|  ListDrivingSch.objects.filter(Q(contact_no__icontains=query), approved=False) |  ListDrivingSch.objects.filter(Q(region__icontains=query), approved=False)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
    
    
# request driving sch
 


class DetailRequestDrivingSch(UserPassesTestMixin,  LoginRequiredMixin, DetailView):
    model = RequestDrivingSch
    form_class = ReqDrvSchForm 
    context_object_name = 'req_drv_sch'
    template_name = 'our_services/req_driving_sch/req_drv_sch_detail.html'
    
    # contains approve or unapprove
    def post(self, request, *args, **kwargs):
        user = request.user
        req_drv_sch = self.get_object()
        if user.is_staff or user.is_superuser:
            req_drv_sch.approved = not req_drv_sch.approved 
            req_drv_sch.save()
            if req_drv_sch.approved == False:
                messages.success(request, 'UnApproved')
            else:
                messages.success(request, 'Approved')
            return redirect(self.request.path_info)
        
        messages.error(request, 'Error, Try Again!')
        return redirect(self.request.path_info)

 
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

 

class DeleteRequestDrivingSch(UserPassesTestMixin, DeleteView, LoginRequiredMixin):
    model = RequestDrivingSch
    context_object_name = 'req_drv_sch'
    template_name = 'our_services/req_driving_sch/req_drv_sch_delete.html'
    
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser :
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
            
    def get_success_url(self):
        messages.success(self.request, "Driving Request  Deleted")
        return reverse('approved-req-drv-sch')



class RequestDrivingSchApproved(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = RequestDrivingSch
    context_object_name = 'req_drv_sch'
    template_name = 'our_services/req_driving_sch/req_drv_sch_approved.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(approved=True).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
 
class RequestDrivingSchUnApproved(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = RequestDrivingSch
    context_object_name = 'req_drv_sch'
    template_name = 'our_services/req_driving_sch/req_drv_sch_unapproved.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(approved=False).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False




# search request driving sch
class  SearchApprovedRequestDrivingSch(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    
    model =  RequestDrivingSch
    context_object_name = 'req_drv_sch'
    template_name = 'our_services/req_driving_sch/req_drv_sch_search_approved.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = RequestDrivingSch.objects.filter(Q(name__icontains=query), approved=True)|  RequestDrivingSch.objects.filter(Q(location__icontains=query), approved=True) |    RequestDrivingSch.objects.filter(Q(email__icontains=query), approved=True)|    RequestDrivingSch.objects.filter(Q(contact_no__icontains=query), approved=True)|  RequestDrivingSch.objects.filter(Q(region__icontains=query), approved=True)|  RequestDrivingSch.objects.filter(Q(budget__icontains=query), approved=True) |  RequestDrivingSch.objects.filter(Q(anything_else__icontains=query), approved=True)
            
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

       
     
class SearchUnApprovedRequestDrivingSch(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    
    model =  RequestDrivingSch
    context_object_name = 'req_drv_sch'
    template_name = 'our_services/req_driving_sch/req_drv_sch_search_unapproved.html'
    paginate_by = 50 

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = RequestDrivingSch.objects.filter(Q(name__icontains=query), approved=False)|  RequestDrivingSch.objects.filter(Q(location__icontains=query), approved=False) |    RequestDrivingSch.objects.filter(Q(email__icontains=query), approved=False)|    RequestDrivingSch.objects.filter(Q(contact_no__icontains=query), approved=False)|  RequestDrivingSch.objects.filter(Q(region__icontains=query), approved=False)|  RequestDrivingSch.objects.filter(Q(budget__icontains=query), approved=False) |  RequestDrivingSch.objects.filter(Q(anything_else__icontains=query), approved=False)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

       
     
 

# list car for rent 
 


class DetailListingCarRental(UserPassesTestMixin,  LoginRequiredMixin, DetailView):
    model = ListCarRental
    form_class = ListCarRentalForm 
    context_object_name = 'listing_car_rent'
    template_name = 'our_services/listing_car_rent/listing_car_rent_detail.html'
    
    #approve and unapprove
    def post(self, request, *args, **kwargs):
        user = request.user
        listing_car_rent = self.get_object()
        
        if user.is_staff or user.is_superuser:
            listing_car_rent.approved = not listing_car_rent.approved 
            listing_car_rent.save()
            if listing_car_rent.approved == False:
                messages.success(request, 'UnApproved')
            else:
                messages.success(request, 'Approved')
            return redirect(self.request.path_info)
        
        messages.error(request, 'Error, Try Again!')
        return redirect(self.request.path_info)

 
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

 

class DeleteListingCarRental(UserPassesTestMixin,  DeleteView, LoginRequiredMixin):
    model = ListCarRental
    context_object_name = 'listing_car_rent'
    template_name = 'our_services/listing_car_rent/listing_car_rent_delete.html'
    
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser :
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False
            
    def get_success_url(self):
        messages.success(self.request, "Driving Request  Deleted")
        return reverse('list-approved-car-rental')



class ListingCarRentalApproved(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = ListCarRental
    context_object_name = 'listing_car_rent'
    template_name = 'our_services/listing_car_rent/listing_car_rent_approved.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(approved=True).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False


class ListingCarRentalUnApproved(UserPassesTestMixin,  LoginRequiredMixin, ListView):
    model = ListCarRental
    context_object_name = 'listing_car_rent'
    template_name = 'our_services/listing_car_rent/listing_car_rent_unapproved.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(approved=False).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False




# search rent out your car
class  SearchApprovedListingCarRental(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    
    model =  ListCarRental
    context_object_name = 'listing_car_rent'
    template_name = 'our_services/listing_car_rent/listing_car_rent_search_approved.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = ListCarRental.objects.filter(Q(car__icontains=query), approved=True)|  ListCarRental.objects.filter(Q(description__icontains=query), approved=True) |    ListCarRental.objects.filter(Q(rate__icontains=query), approved=True)|    ListCarRental.objects.filter(Q(per__icontains=query), approved=True)|  ListCarRental.objects.filter(Q(location__icontains=query), approved=True)|  ListCarRental.objects.filter(Q(contact_no__icontains=query), approved=True) |  ListCarRental.objects.filter(Q(region__icontains=query), approved=True)|  ListCarRental.objects.filter(Q(color__icontains=query), approved=True)|  ListCarRental.objects.filter(Q(interior_color__icontains=query), approved=True)|  ListCarRental.objects.filter(Q(accessories__icontains=query), approved=True)|  ListCarRental.objects.filter(Q(email__icontains=query), approved=True)
               
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

       
     
class SearchUnApprovedListingCarRental(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    
    model =  ListCarRental
    context_object_name = 'listing_car_rent'
    template_name = 'our_services/listing_car_rent/listing_car_rent_search_unapproved.html'
    paginate_by = 50 

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = ListCarRental.objects.filter(Q(car__icontains=query), approved=False)|  ListCarRental.objects.filter(Q(description__icontains=query), approved=False) |    ListCarRental.objects.filter(Q(rate__icontains=query), approved=False)|    ListCarRental.objects.filter(Q(per__icontains=query), approved=False)|  ListCarRental.objects.filter(Q(location__icontains=query), approved=False)|  ListCarRental.objects.filter(Q(contact_no__icontains=query), approved=False) |  ListCarRental.objects.filter(Q(region__icontains=query), approved=False)|  ListCarRental.objects.filter(Q(color__icontains=query), approved=False)|  ListCarRental.objects.filter(Q(interior_color__icontains=query), approved=False)|  ListCarRental.objects.filter(Q(accessories__icontains=query), approved=False)|  ListCarRental.objects.filter(Q(email__icontains=query), approved=False)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:  
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')
        return False

       
     
 