from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def singup_view(request):
    return render(request, 'singup.html')