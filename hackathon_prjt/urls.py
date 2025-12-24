from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('signout/',views.signout,name='signout'),
    path('signup_doc/',views.signup_doc,name='signup_doc'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
]