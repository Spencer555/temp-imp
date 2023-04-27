from django import forms 
from OurServices.models import ShipCarForUsSell, LetUsSellYourCar, ContactUsForEnquires, CarRental, CarRentalImage, RentCar, ListAccessories, ListCarRental, ListDrivingSch, RequestDrivingSch




class ShipCarForUsSellForm(forms.ModelForm):
    class Meta:
        model = ShipCarForUsSell
        fields = '__all__'

        widgets ={
            'your_name':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Your Name', 'aria-label':"Your Name", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'email':forms.EmailInput(attrs={'class':'form-control chk-box ', 'placeholder':'Email', "required":'true' }),
            
            'contact':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Contact', 'aria-label':"Contact", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'title':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Car Title', 'aria-label':"Car Title", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'contact_no':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Phone No', 'aria-label':"Phone No", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'makes_and_model':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Make & Model','id':"inputGroupSelect01 ", "required":'true' }),
            
            'country':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Make & Model','id':"inputGroupSelect01 ", "required":'true' }),
            
            'condition':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Condition','id':"inputGroupSelect01 ", "required":'true' }),
            
            'transmission':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Transmission','id':"inputGroupSelect01 ", "required":'true' }),
            
            'fuel':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Fuel','id':"inputGroupSelect01 ", "required":'true' }),
            
            'steering':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Steering','id':"inputGroupSelect01 ", "required":'true' }),
            
            'year_manufactured':forms.NumberInput(attrs={'class':'form-control chk-box ', 'placeholder':'Year Manufactured', "required":'true' }),
            
            'price':forms.NumberInput(attrs={'class':'form-control chk-box ', 'placeholder':'Price', "required":'true' }),
            
            'mileage':forms.NumberInput(attrs={'class':'form-control chk-box ', 'placeholder':'mileage', "required":'true' }),
            
            'color':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Exterior Color', 'aria-label':"Color", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'interior_color':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Interior Color', 'aria-label':"Interior Color", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'location':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Location', 'aria-label':"Location", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'accessories':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Accessories', 'aria-label':"Accessories", 'aria-describedby':"basic-addon1", 'rows':'2', "required":'true' }),

            'description':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Description', 'rows':'3', "required":'true'}),

            'anything_u_want_to_tell_us':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Anything You Want To Tell Us', 'rows':'3', "required":'true'}),

            'registered':forms.CheckboxInput(attrs={'class':'form-check-input chk-box nice-blue','type':'checkbox',  'for':"inlineCheckbox1"}),
            
            'duty_paid':forms.CheckboxInput(attrs={'class':'form-check-input chk-box nice-blue','type':'checkbox',  'for':"inlineCheckbox1"}),
            
            'attended_to':forms.CheckboxInput(attrs={'class':'form-check-input chk-box nice-blue','type':'checkbox',  'for':"inlineCheckbox1"}),

            'main_image':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_1':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_2':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_3':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_4':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            

        }
        
        
        
class LetUsSellYourCarForm(forms.ModelForm):
    class Meta:
        model = LetUsSellYourCar
        fields = '__all__'
        
        widgets ={
            'your_name':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Your Name', 'aria-label':"Your Name", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            
            'contact':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Contact', 'aria-label':"Contact", 'aria-describedby':"basic-addon1", "required":'true' }),
            
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

            'anything_u_want_to_tell_us':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Anything You Want To Tell Us', 'rows':'3', "required":'true'}),

            'registered':forms.CheckboxInput(attrs={'class':'form-check-input chk-box nice-blue','type':'checkbox',  'for':"inlineCheckbox1"}),
            
            'duty_paid':forms.CheckboxInput(attrs={'class':'form-check-input chk-box nice-blue','type':'checkbox',  'for':"inlineCheckbox1"}),
            
            'attended_to':forms.CheckboxInput(attrs={'class':'form-check-input chk-box nice-blue','type':'checkbox',  'for':"inlineCheckbox1"}),

            'main_image':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_1':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_2':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_3':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_4':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'email':forms.EmailInput(attrs={'class':'form-control chk-box ', 'placeholder':'Email', "required":'true' }),


        }
        
        
        
        
class ContactUsForEnquiresForm(forms.ModelForm):
    class Meta:
        model = ContactUsForEnquires
        fields = '__all__'
        
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Full Name', 'aria-label':"Full Name", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'contact':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Phone No', 'aria-label':"Phone No", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'email':forms.EmailInput(attrs={'class':'form-control chk-box ', 'placeholder':'Price', "required":'true' }),

            'enquiry':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Enquiry', 'rows':'3', "required":'true'}),




        }


        
        
        
        
        
class CarRentalForm(forms.ModelForm):
    class Meta:
        model = CarRental
        fields = '__all__'
        
        widgets ={
            'car':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Car Name', 'aria-label':"Car Name", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'contact_no':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Phone No', 'aria-label':"Phone No", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'region':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Region','id':"inputGroupSelect01 ", "required":'true' }),
            
            'per':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Per','id':"inputGroupSelect01 ", "required":'true' }),
            
            'rate':forms.NumberInput(attrs={'class':'form-control chk-box ', 'placeholder':'Rate', "required":'true' }),
            
            'color':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Exterior Color', 'aria-label':"Color", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'interior_color':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Interior Color', 'aria-label':"Interior Color", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'location':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Location', 'aria-label':"Location", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'accessories':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Accessories', 'aria-label':"Accessories", 'aria-describedby':"basic-addon1", 'rows':'2', "required":'true' }),
            
            'description':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Description', 'aria-label':"Accessories", 'aria-describedby':"basic-addon1", 'rows':'2', "required":'true' }),
            
            'main_image':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1"}),
            
            'user':forms.Select(attrs={'hidden':'true' }),

        }
        
         
        
class CarRentalImageForm(forms.ModelForm):
    class Meta:
        model = CarRentalImage
        fields = '__all__'
        
        
class RentCarForm(forms.ModelForm):
    class Meta:
        model = RentCar
        fields = '__all__'
        
        
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':' Name', 'aria-label':" Name", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'email':forms.EmailInput(attrs={'class':'form-control chk-box ', 'placeholder':'Email', "required":'true' }),
            
            'contact':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Contact', 'aria-label':"Contact", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'location':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Location', 'aria-label':"Location", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'region':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Region','id':"inputGroupSelect01 ", "required":'true' }),
            
            

        }
        
        
        
  
class ListAccessoriesForm(forms.ModelForm):
    
    class Meta:
        model = ListAccessories
        fields = '__all__'


        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Full Name', 'aria-label':"Full Name", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'contact_no':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Phone No', 'aria-label':"Phone No", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'price':forms.NumberInput(attrs={'class':'form-control chk-box ', 'placeholder':'Price', "required":'true' }),

            'description':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Description', 'rows':'3', "required":'true'}),
    

            'main_image':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_1':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_2':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_3':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_4':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'email':forms.EmailInput(attrs={'class':'form-control chk-box ', 'placeholder':'Email', "required":'true' }),
            
            'approved':forms.CheckboxInput(attrs={'class':'form-check-input chk-box nice-blue','type':'checkbox',  'for':"inlineCheckbox1"}),
            
            'region':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Region','id':"inputGroupSelect01 ", "required":'true' }),


            

        }

     
class ListCarRentalForm(forms.ModelForm):
    class Meta:
        model = ListCarRental
        fields = '__all__'
        
        widgets ={
            'car':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Car Name', 'aria-label':"Car Name", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'email':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Email', 'aria-label':"Email", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'contact_no':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Phone No', 'aria-label':"Phone No", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'region':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Region','id':"inputGroupSelect01 ", "required":'true' }),
            
            'per':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Per','id':"inputGroupSelect01 ", "required":'true' }),
            
            'rate':forms.NumberInput(attrs={'class':'form-control chk-box ', 'placeholder':'Rate', "required":'true' }),
            
            'color':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Exterior Color', 'aria-label':"Color", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'interior_color':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Interior Color', 'aria-label':"Interior Color", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'location':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Location', 'aria-label':"Location", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'accessories':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Accessories', 'aria-label':"Accessories", 'aria-describedby':"basic-addon1", 'rows':'2', "required":'true' }),
            
            'description':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Description', 'aria-label':"Accessories", 'aria-describedby':"basic-addon1", 'rows':'2', "required":'true' }),
            
            'main_image':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1"}),
            
            'approved':forms.CheckboxInput(attrs={'class':'form-check-input chk-box nice-blue','type':'checkbox',  'for':"inlineCheckbox1"}),
            
            'image_1':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_2':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_3':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),
            
            'image_4':forms.FileInput(attrs={'class':'form-control chk-box nice-blue',  'for':"inlineCheckbox1" ,'accept':"image/*"}),


        }
     
class ReqDrvSchForm(forms.ModelForm):
    class Meta:
        model = RequestDrivingSch
        fields = '__all__'
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Name', 'aria-label':"Name", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'location':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Location', 'aria-label':"Location", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'contact_no':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Phone No', 'aria-label':"Phone No", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'region':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Region','id':"inputGroupSelect01 ", "required":'true' }),
            
            'email':forms.EmailInput(attrs={'class':'form-control chk-box ', 'placeholder':'Email', "required":'true' }),
           
            'budget':forms.NumberInput(attrs={'class':'form-control chk-box ', 'placeholder':'Budget', "required":'true' }),

            'anything_else':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Anything You Want To Tell Us', 'aria-label':"Accessories", 'aria-describedby':"basic-addon1", 'rows':'2'  }),
             
             

        }
     
class ListDrivingSchForm(forms.ModelForm):
    class Meta:
        model = ListDrivingSch
        fields = '__all__'
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Name', 'aria-label':"Name", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'driving_sch_name':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'School Name', 'aria-label':"School Name", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'location':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Location', 'aria-label':"Location", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'contact_no':forms.TextInput(attrs={'class':'form-control chk-box ', 'placeholder':'Phone No', 'aria-label':"Phone No", 'aria-describedby':"basic-addon1", "required":'true' }),
            
            'region':forms.Select(attrs={'class':'form-control chk-box ', 'placeholder':'Region','id':"inputGroupSelect01 ", "required":'true' }),
            
            'email':forms.EmailInput(attrs={'class':'form-control chk-box ', 'placeholder':'Email', "required":'true' }),
            
            'services_offered':forms.Textarea(attrs={'class':'form-control chk-box ', 'placeholder':'Services Offered', 'aria-label':"Services Offered", 'aria-describedby':"basic-addon1", 'rows':'2', "required":'true' }),
            
            'approved':forms.CheckboxInput(attrs={'class':'form-check-input chk-box nice-blue','type':'checkbox',  'for':"inlineCheckbox1"}),
             

        }
     