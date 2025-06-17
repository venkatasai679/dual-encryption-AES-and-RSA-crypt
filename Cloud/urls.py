from django.urls import path
from . import views

urlpatterns = [
    path('cloudhome/', views.cloudhome, name='cloudhome'),
    path('allfiles/', views.allfiles, name='allfiles'),
    path('requests/', views.requests, name='requests'),
    path('viewusers/', views.viewusers, name='viewusers'),
    path('sendotp/<int:id>/', views.sendotp, name='sendotp'),
    

]
