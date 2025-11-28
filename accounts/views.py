from django.shortcuts import render
from .application.create_user import CreateUser
from .infrastructure.user_repository import DjangoUserRepository

def login_view(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f'Username: {email}, Password: {password}')

    return render(request, 'login.html')

def singup_view(request):

    if request.method == 'POST':
        password = request.POST.get('password')
        email = request.POST.get('email')

        repository = DjangoUserRepository()
        create_user = CreateUser(repository)

        created_user = create_user.execute(email, password)

        print(f'Created User: {created_user.email.__str__()}')

    return render(request, 'singup.html')