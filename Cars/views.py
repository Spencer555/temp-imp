from django.shortcuts import redirect
from Cars.models import Car, CarEnquiry, CarImage
from Cars.forms import CarEnquiryForm, CarForm, CarImageForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.db.models import Q
from django.urls import reverse
from Analytics.views import ourAnalytics
# Create your views here.
 

 
class CreateCarView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Car
    form_class = CarForm
    context_object_name = 'car'
    template_name = 'car/create_car.html'
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

 
    def get_success_url(self):
        messages.success(self.request, 'Car Created')
        return reverse('create-car')       
     
             
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')

        return False
    

class UpdateCarView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Car
    template_name = 'car/update_car.html'
    form_class = CarForm 
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

 
    def get_success_url(self):
        messages.success(self.request, 'Car Updated')
        return reverse('detail-car', kwargs={'slug':self.get_object().slug, 'pk':self.get_object().id})       
     
             
    def test_func(self):
        user = self.request.user 
        car = self.get_object()
        if user.is_staff or user.is_superuser or car.user:
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')

        return False
    
         
# contains add car image, delete car image, add car enquiry
class DetailCarView(DetailView):
    model = Car
    context_object_name = 'car'
    template_name = 'car/detail_car.html'
    
    def get_context_data(self, **kwargs):
            data = super().get_context_data(**kwargs)
            car = self.get_object()
            data['car_image'] = CarImage.objects.filter(car=car)
            return data
     
    def post(self, request, *args, **kwagrs):
        user = request.user
        
        # add car image
        if request.POST['type'] == 'car_image':
    
            if user.is_staff or user.is_superuser :
                car = self.get_object()
                request.POST._mutable = True
                request.POST['user'] = user 
                request.POST['car'] = car
                request.FILES['image'] = request.FILES['image']
                request.POST._mutable = False

                image_form = CarImageForm(request.POST, request.FILES)
                if image_form.is_valid():
                    image_form.save()
                    messages.success(request, 'Image Added')
                    return redirect(self.request.path_info)
                messages.warning(request, 'Image Not Added Try Again!')
                return redirect(self.request.path_info)
            
            messages.warning(request, 'Image Not Added Try Again!')
            return redirect(self.request.path_info)
      
        #    delete car image
        elif request.POST['type'] == 'delete':

            if user.is_staff or user.is_superuser :
                id = request.POST['id'] 
                slug = request.POST['slug'] 
                
                image =  CarImage.objects.filter(id=id, slug=slug).first()
            
            
                if image:
                    image.delete()
                    messages.success(request, 'Image Deleted')
                    return redirect(self.request.path_info)
                else:
                    messages.warning(request, 'Not Deleted! Pls Try Again')
                    return redirect(self.request.path_info)
      
       
        # add car enquiry
        elif  request.POST['type'] == 'car_enquiry':
            
            car = self.get_object()
            request.POST._mutable = True
            request.POST['car'] = car
            request.POST._mutable = False
 
            car_enquiry_form = CarEnquiryForm(request.POST)
            if  car_enquiry_form.is_valid():
                car_enquiry_form.save()
                messages.success(request, 'Enquiry Sent')
                return redirect(self.request.path_info)
        
            else:
                if 'contact_no' in car_enquiry_form.errors:
                    error = car_enquiry_form.errors['contact_no'][0]
                    messages.warning(request, f'Not Sent!  {error}')
                    return redirect(self.request.path_info)
        
                else:
                    messages.warning(request, 'Error! Enquiry Not Sent')
                    return redirect(self.request.path_info)

        messages.warning(request, 'Error Please Try Again')
        return redirect(self.request.path_info)


         
       

class ListCarView(ListView):
    model = Car
    context_object_name = 'car'
    template_name = 'car/car_list.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        ourAnalytics(self.request)
        queryset = Car.objects.all().order_by('-created')
        return queryset
 

class DeleteCarView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    context_object_name = 'car'
    template_name = 'car/car_delete.html'
    

    def test_func(self):
        
        user = self.request.user 
        car = self.get_object()
        if user.is_staff or user.is_superuser or car.user:
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')

        return False
        
    def get_success_url(self):
        messages.success(self.request, 'Car Deleted')
        return reverse('list-car')


  

#car enquiry
class ListCarEnquiryAttendedTo(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model = CarEnquiry
    context_object_name = 'car_enquiry'
    template_name = 'car/car_enquiry/list_car_enquiry_attended_to.html'
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



class ListCarEnquiryNotAttendedTo(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model = CarEnquiry
    context_object_name = 'car_enquiry'
    template_name = 'car/car_enquiry/list_car_enquiry_not_attended_to.html'
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

class DeleteCarEnquiry(UserPassesTestMixin,  LoginRequiredMixin, DeleteView):
    model = CarEnquiry
    context_object_name = 'car_enquiry'
    template_name = 'car/car_enquiry/car_enquiry_delete.html'

    
    def get_success_url(self):
        messages.success(self.request, 'Car Enquiry Deleted')
        return reverse('list-car-enquiry-attended-to')

    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser :
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')

        return False



# contains attended to
class DetailCarEnquiry(LoginRequiredMixin, UserPassesTestMixin,DetailView):
    model = CarEnquiry
    context_object_name = 'car_enquiry'
    template_name = 'car/car_enquiry/detail_car_enquiry.html'
    
    # attend to and unattend to
    def post(self, request, *args, **kwargs):
        user = request.user
        car_enquiry = self.get_object()
        if user.is_staff or user.is_superuser:
            car_enquiry.attended_to = not car_enquiry.attended_to 
            car_enquiry.save()
            if car_enquiry.attended_to == False:
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

    
    
# search 
 
class CarAttendedToEnquirySearch(UserPassesTestMixin, LoginRequiredMixin, ListView):       
    model =  CarEnquiry
    context_object_name = 'car_enquiry'
    template_name = 'car/car_enquiry/search_car_enquiry_attended_to.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = CarEnquiry.objects.filter(Q(name__icontains=query), attended_to=True) |  CarEnquiry.objects.filter(Q(contact_no__icontains=query), attended_to=True) | CarEnquiry.objects.filter(Q(message__icontains=query), attended_to=True) | CarEnquiry.objects.filter(Q(car__makes_and_model__icontains=query), attended_to=True)| CarEnquiry.objects.filter(Q(email__icontains=query), attended_to=True)
                
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
        
         
     

class CarNotAttendedToEnquirySearch(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model =  CarEnquiry
    context_object_name = 'car_enquiry'
    template_name = 'car/car_enquiry/search_car_enquiry_not_attended_to.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = CarEnquiry.objects.filter(Q(name__icontains=query), attended_to=False) |  CarEnquiry.objects.filter(Q(contact_no__icontains=query), attended_to=False) | CarEnquiry.objects.filter(Q(message__icontains=query), attended_to=False) | CarEnquiry.objects.filter(Q(car__makes_and_model__icontains=query), attended_to=False) | CarEnquiry.objects.filter(Q(email__icontains=query), attended_to=False)
                
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
        
         
        
        
        
