from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from auth_system.forms import LoginForm, RegisterForm
# Create your views here.
class CustomLoginView(LoginView):
    template_name = "auth_system/login_page.html"
    form_class = LoginForm

class CustomRegisterView(CreateView):
    template_name = "auth_system/register_page.html"
    form_class = RegisterForm
    success_url = "login"

