from django.shortcuts import render

def frontpage(request):
    return render(request, 'core/frontpage.html')

def login(request):
    return render(request, 'core/login.html')