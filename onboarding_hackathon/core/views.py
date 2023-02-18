from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

#from employee.models import Employee

def frontpage(request):
    return render(request, 'core/frontpage.html')

def login(request):
    if request.method == 'POST':
        identifier = request.POST['identifier']
        password = request.POST['password']
        user = authenticate(identifier=identifier, password=password)
        if user is not None:
            if user.is_active:
                return redirect('/frontpage/')
            else:
                raise ValueError('Something trouble')
    
    return render(request, 'core/login.html')