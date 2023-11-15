from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('bed/',views.bedroom_spline,name='bed_spline'),
    path('about_info/',views.about_spline,name='about_spline'),
    path('about/',views.about,name='about'),
    path('projects/',views.projects,name='projects'),
    path('contact/',views.contact,name='contact')
]