from django import forms 
from Accessories.models import Accessories, AccessoriesImages, AccessoriesEnquiry
 
class AccessoriesForm(forms.ModelForm):
    
    class Meta:
        model = Accessories
        fields = '__all__'


        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Full Name', 'aria-label':"Full Name", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'contact_no':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Phone No', 'aria-label':"Phone No", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'price':forms.NumberInput(attrs={'class':'form-control chk-box ', 'placeholder':'Price', "required":'true' }),

            'description':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Description', 'rows':'3', "required":'true'}),


            'main_image':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'user':forms.TextInput(attrs={'class':'d-none' }),


        }


class AccessoriesImageForm(forms.ModelForm):
    
    class Meta:
        model = AccessoriesImages
        fields = '__all__'

class AccessoriesEnquiryForm(forms.ModelForm):
    
    class Meta:
        model = AccessoriesEnquiry
        fields = '__all__'