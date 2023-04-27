from django import forms 
from Cars.models import CarEnquiry, Car, CarImage



class CarForm(forms.ModelForm):
    class Meta:
        model= Car 
        fields = '__all__'
        
        widgets ={
            
            'title':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Car Title', 'aria-label':"Car Title", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'contact_no':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Phone No', 'aria-label':"Phone No", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'makes_and_model':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Make & Model','id':"inputGroupSelect01 ", "required":'true' }),
            
            'condition':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Condition','id':"inputGroupSelect01 ", "required":'true' }),
            
            'transmission':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Transmission','id':"inputGroupSelect01 ", "required":'true' }),
            
            'fuel':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Fuel','id':"inputGroupSelect01 ", "required":'true' }),
            
            'region':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Region','id':"inputGroupSelect01 ", "required":'true' }),
            
            'steering':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Steering','id':"inputGroupSelect01 ", "required":'true' }),
            
            'year_manufactured':forms.NumberInput(attrs={'class':'form-control chk-box ', 'placeholder':'Year Manufactured', "required":'true' }),
            
            'price':forms.NumberInput(attrs={'class':'form-control chk-box ', 'placeholder':'Price', "required":'true' }),
            
            'mileage':forms.NumberInput(attrs={'class':'form-control chk-box ', 'placeholder':'mileage', "required":'true' }),
            
            'color':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Exterior Color', 'aria-label':"Color", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'interior_color':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Interior Color', 'aria-label':"Interior Color", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'location':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Location', 'aria-label':"Location", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'accessories':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Accessories', 'aria-label':"Accessories", 'aria-describedby':"basic-addon1", 'rows':'2', "required":'true' }),

            'description':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Description', 'rows':'3', "required":'true'}),

            'registered':forms.CheckboxInput(attrs={'class':'form-check-input chk-box nice-blue','type':'checkbox',  'for':"inlineCheckbox1"}),
            
            'duty_paid':forms.CheckboxInput(attrs={'class':'form-check-input chk-box nice-blue','type':'checkbox',  'for':"inlineCheckbox1"}),

            'main_image':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1"}),
            'user':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Steering','hidden':"true" }),

        }
 
 
class CarImageForm(forms.ModelForm):
    class Meta:
        model= CarImage 
        fields = ('user', 'image', 'car')
        
        

class CarEnquiryForm(forms.ModelForm):
    class Meta:
        model= CarEnquiry 
        fields = '__all__'
        
