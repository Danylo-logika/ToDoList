from django.urls import path
from auth_system import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('register/', views.CustomRegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]