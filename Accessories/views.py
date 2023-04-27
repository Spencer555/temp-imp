from django.shortcuts import  redirect
from Accessories.models import Accessories, AccessoriesImages, AccessoriesEnquiry
from Accessories.forms import AccessoriesForm, AccessoriesImageForm, AccessoriesEnquiryForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.db.models import Q
# Create your views here.
 

class CreateAccessories(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Accessories
    form_class = AccessoriesForm
    context_object_name = 'accessory'
    template_name = 'accessories/create_accessories.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

 
    def get_success_url(self):
        messages.success(self.request, 'Accessory Created')
        return reverse('create-accessory')       

        
    def test_func(self):
        user = self.request.user 
        if user.is_staff or user.is_superuser:
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')

        return False


# contains upload accessory image, delete image, create accessory enquiry
class DetailAccessories(DetailView):
    model = Accessories
    context_object_name = 'accessory'
    template_name = 'accessories/detail_accessories.html'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        accessories = self.get_object()
        data['accessory_image'] = AccessoriesImages.objects.filter(accessories=accessories)
        return data
    
    def post(self, request, *args, **kwagrs):
        user = request.user
        # add image
        if request.POST['type'] == 'accessory_image':
            if user == user.is_staff or user.is_superuser :
                accessory = self.get_object()
                request.POST._mutable = True
                request.POST['user'] = user 
                request.POST['accessories'] = accessory
                request.FILES['image'] = request.FILES['image']
                request.POST._mutable = False

                accessory_image_form = AccessoriesImageForm(request.POST, request.FILES)
                if accessory_image_form.is_valid():
                    accessory_image_form.save()
                    messages.success(request, 'Image Added')
                    return redirect(self.request.path_info)
                messages.warning(request, 'Image Not Added Try Again!')
                return redirect(self.request.path_info)
            
            messages.warning(request, 'Image Not Added Try Again!')
            return redirect(self.request.path_info)
      
            # delete acc image    
        elif request.POST['type'] == 'delete':
            id = request.POST['id'] 
            slug = request.POST['slug'] 
            
            image =  AccessoriesImages.objects.filter(id=id, slug=slug).first()
            
            
            if image:
                image.delete()
                messages.success(request, 'Image Deleted')
                return redirect(self.request.path_info)
            else:
                messages.warning(request, 'Not Deleted! Pls Try Again')
                return redirect(self.request.path_info)

      

       
        # add accessory enquiry
        elif request.POST['type'] == 'accessory_enquiry':
            accessory = self.get_object()
            request.POST._mutable = True
            request.POST['accessory'] = accessory
            request.POST._mutable = False

            accessory_enquiry_form = AccessoriesEnquiryForm(request.POST)
            if  accessory_enquiry_form.is_valid():
                accessory_enquiry_form.save()
                messages.success(request, 'Enquiry Sent')
                return redirect(self.request.path_info)
            
            else:
                if 'contact_no' in accessory_enquiry_form.errors:
                    error = accessory_enquiry_form.errors['contact_no'][0]
                    messages.warning(request, f'Not Sent!  {error}')
                    return redirect(self.request.path_info)
    
                else:
                    messages.warning(request, 'Error! Enquiry Not Sent')
                    return redirect(self.request.path_info)        
        
        
        messages.warning(request, 'Error Please Try Again')
        return redirect(self.request.path_info)

        
       

class ListAccessories(ListView):
    model = Accessories
    context_object_name = 'accessory'
    template_name = 'accessories/list_accessories.html'
    paginate_by = 50
    queryset = Accessories.objects.all().order_by('-created')


class UpdateAccessories(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Accessories
    form_class = AccessoriesForm
    context_object_name = 'accessory'
    template_name = 'accessories/update_accessories.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

 
    def get_success_url(self):
        messages.success(self.request, 'Accessory Updated')
        return reverse('detail-accessory', kwargs={'slug':self.get_object().slug, 'pk':self.get_object().id})       

    
    def test_func(self):
        user = self.request.user 
        accessory = self.get_object()
        if user.is_staff or user.is_superuser or accessory.user:
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')

        return False


class DeleteAccessories(UserPassesTestMixin,  LoginRequiredMixin, DeleteView):
    model = Accessories
    context_object_name = 'accessory'
    template_name = 'accessories/accessories_delete.html'

    def test_func(self):
        user = self.request.user 
        accesory = self.get_object()
        if user.is_staff or user.is_superuser or accesory.user:
            return True
        messages.warning(self.request, 'Not Authorized Permission Denied')

        return False
        
    def get_success_url(self):
        messages.success(self.request, 'Accessory Deleted')
        return reverse('list-accessory')



 
# accessory enquiry attended to
class ListAccessoriesEnquiryAttendedTo(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = AccessoriesEnquiry
    context_object_name = 'accessories_enquiry'
    template_name = 'accessories/accessories_enquiry/list_accessories_enquiry_attended_to.html'
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

# accessory enquiry not attended to

class ListAccessoriesEnquiryNotAttendedTo(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = AccessoriesEnquiry
    context_object_name = 'accessories_enquiry'
    template_name = 'accessories/accessories_enquiry/list_accessories_enquiry_not_attended_to.html'
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

 

class DeleteAccessoriesEnquiry(UserPassesTestMixin, DeleteView, LoginRequiredMixin):
    model = AccessoriesEnquiry
    context_object_name = 'acc_enquiry'
    template_name = 'accessories/accessories_enquiry/accessories_enquiry_delete.html'
    
    
    def get_success_url(self):
        messages.success(self.request, 'Accessory Enquiry Deleted')
        return reverse('list-accessory-attended-to')

    def test_func(self):
            user = self.request.user 
            if user.is_staff or user.is_superuser :
                return True
            messages.warning(self.request, 'Not Authorized Permission Denied')

            return False


# contains attended to
class DetailAccessoriesEnquiry(LoginRequiredMixin, UserPassesTestMixin,DetailView):
    model = AccessoriesEnquiry
    context_object_name = 'acc_enquiry'
    template_name = 'accessories/accessories_enquiry/detail_accessories_enquiry.html'
    
    # attend to or unattend to
    def post(self, request, *args, **kwargs):
        user = request.user
        accessory_enquiry = self.get_object()
        if user.is_staff or user.is_superuser:
            accessory_enquiry.attended_to = not accessory_enquiry.attended_to 
            accessory_enquiry.save()
            if accessory_enquiry.attended_to == False:
                messages.success(request, 'Unattended To')
                return redirect(self.request.path_info)

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
class AccessoriesAttendedToEnquirySearch(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model =  Accessories
    context_object_name = 'results'
    template_name = 'accessories/accessories_enquiry/search_accessories_attended.html'
    paginate_by = 50
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = AccessoriesEnquiry.objects.filter(Q(name__icontains=query), attended_to=True) |  AccessoriesEnquiry.objects.filter(Q(contact_no__icontains=query), attended_to=True) | AccessoriesEnquiry.objects.filter(Q(message__icontains=query), attended_to=True) | AccessoriesEnquiry.objects.filter(Q(accessory__name__icontains=query), attended_to=True) | AccessoriesEnquiry.objects.filter(Q(email__icontains=query), attended_to=True)
            
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

                 
        
        
         
        

class AccessoriesNotAttendedToEnquirySearch(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model =  Accessories
    context_object_name = 'results'
    template_name = 'accessories/accessories_enquiry/search_accessories_not_attended.html'
    paginate_by = 50

        
       
        
      
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = AccessoriesEnquiry.objects.filter(Q(name__icontains=query), attended_to=False) |  AccessoriesEnquiry.objects.filter(Q(contact_no__icontains=query), attended_to=False) | AccessoriesEnquiry.objects.filter(Q(message__icontains=query), attended_to=False) | AccessoriesEnquiry.objects.filter(Q(accessory__name__icontains=query), attended_to=False) | AccessoriesEnquiry.objects.filter(Q(email__icontains=query), attended_to=False)
            
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

        