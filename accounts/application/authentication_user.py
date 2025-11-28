from django.http import HttpRequest
from domain.auth.email import Email
from domain.auth.password import Password

from django.contrib.auth import authenticate, login

class AuthenticateEmailUser:

    def __init__(self, email: str, password: str, request: HttpRequest):
        self.email = email
        self.password = password
        self.request = request

    def authenticate_user(self):
        email_obj = Email(self.email)
        password_obj = Password(self.password)

        user = authenticate(username=email_obj.value, password=password_obj.value)

        if user is None:
            raise "Usuario ou senha incorretos"
        
        login(self.request, user)

        return user


