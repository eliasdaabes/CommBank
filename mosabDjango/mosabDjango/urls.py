"""
Definition of urls for mosabDjango.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),

    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('list/', views.list, name='list'),
    path('managerSignIn/', views.managerSignIn, name='managerSignIn'),
    path('secretarySignIn/', views.secretarySignIn, name='secretarySignIn'),
    path('volunteerSignIn/', views.volunteerSignIn, name='volunteerSignIn'),
    path('updatePassword/', views.updatePassword, name='updatePassword'),
    path('forgetPassword/', views.forgotPassword, name='forgetPassword'),
]
