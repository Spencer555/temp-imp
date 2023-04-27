from django.shortcuts import render
from django.views.generic import (
    View
)
# terms and conditions
class TermsAndCondtions(View):
    def get(self, request):

        return render(request, 'readonly/terms_and_condition.html')
     

# privacy view
class Privacy(View):
    def get(self, request):

        return render(request, 'readonly/privacy.html')
     

   