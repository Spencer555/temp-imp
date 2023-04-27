from Cars.models import Car 
from Accessories.models import Accessories
from OurServices.models import CarRental
from django.db.models import Q 
from django.views.generic import (
    ListView
) 
  
  
# car search

class CarSearch(ListView):
    model =  Car
    context_object_name = 'car'
    template_name = 'search/search_cars.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = Car.objects.filter(Q(makes_and_model__icontains=query))  | Car.objects.filter(Q(description__icontains=query))  | Car.objects.filter(Q(contact_no__icontains=query))    |Car.objects.filter(Q(region__icontains=query))  |Car.objects.filter(Q(color__icontains=query))  | Car.objects.filter(Q(interior_color__icontains=query)) | Car.objects.filter(Q(accessories__icontains=query))| Car.objects.filter(Q(region__icontains=query)) | Car.objects.filter(Q(title__icontains=query)) | Car.objects.filter(Q(makes_and_model__icontains=query)) | Car.objects.filter(Q(mileage__icontains=query))  | Car.objects.filter(Q(steering__icontains=query))  | Car.objects.filter(Q(transmission__icontains=query)) | Car.objects.filter(Q(fuel__icontains=query))   | Car.objects.filter(Q(year_manufactured__icontains=query)) | Car.objects.filter(Q(price__icontains=query))
                
        return queryset


        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

# accessory search
class AccessoriesSearch(ListView):
    model =  Car
    context_object_name = 'accessory'
    template_name = 'search/search_accessories.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = Accessories.objects.filter(Q(name__icontains=query))  | Accessories.objects.filter(Q(description__icontains=query))  | Accessories.objects.filter(Q(price__icontains=query))  | Accessories.objects.filter(Q(contact_no__icontains=query))
                
        return queryset


        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context


# car rental search

class RentalCarsSearch(ListView):
    model =  Car
    context_object_name = 'car_rental'
    template_name = 'search/search_car_rental.html'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset =  CarRental.objects.filter(Q(car__icontains=query))  | CarRental.objects.filter(Q(description__icontains=query))  | CarRental.objects.filter(Q(contact_no__icontains=query))  | CarRental.objects.filter(Q(region__icontains=query))  | CarRental.objects.filter(Q(rate__icontains=query))  | CarRental.objects.filter(Q(per__icontains=query)) | CarRental.objects.filter(Q(color__icontains=query))  | CarRental.objects.filter(Q(interior_color__icontains=query)) | CarRental.objects.filter(Q(accessories__icontains=query))| CarRental.objects.filter(Q(region__icontains=query))
                
        return queryset


        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] =self.request.GET.get('q')
        return context

 