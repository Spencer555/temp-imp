from django.shortcuts import render, redirect
from django.contrib import messages, auth
 




 
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user =  auth.authenticate(email=email, password=password) 
        print(user)
      
        if  user is not None:
            auth.login(request, user)
            return redirect('list-car')

        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'authentication/login.html')


   