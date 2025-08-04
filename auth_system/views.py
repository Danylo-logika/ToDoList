from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from auth_system.forms import LoginForm, RegisterForm
# Create your views here.
class CustomLoginView(LoginView):
    template_name = "auth_system/login_page.html"
    form_class = LoginForm

class CustomRegisterView(CreateView):
    template_name = "auth_system/register_page.html"
    form_class = RegisterForm
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return response

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')