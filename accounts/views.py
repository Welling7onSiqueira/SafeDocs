from django.shortcuts import render, redirect
from .application.create_user import CreateUser
from .application.authentication_user import AuthenticateEmailUser
from .infrastructure.user_repository import DjangoUserRepository

def login_view(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        authenticator = AuthenticateEmailUser(email, password, request)
        authenticator.authenticate_user()

        return redirect('singup')

    return render(request, 'login.html')

def singup_view(request):

    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')

        repository = DjangoUserRepository()
        create_user = CreateUser(repository)

        created_user = create_user.execute(email, password, confirm_password)

        print(f'Created User: {created_user.email}')

    return render(request, 'singup.html')