from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_page'),
    path('singup/', views.singup_view, name='singup'),
]
