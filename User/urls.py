from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('userhome/', views.userhome, name='userhome'),

    path('logout/', views.logout, name='logout'),
    path('uploadfile/', views.uploadfile, name='uploadfile'),
    path('viewfiles/', views.viewfiles, name='viewfiles'),
    path('viewallfiles/', views.viewallfiles, name='viewallfiles'),
    path('decryptmyfile/<int:id>/', views.decryptmyfile, name='decryptmyfile'),
    path('sendrequest/<int:id>/', views.sendrequest, name='sendrequest'),
    path('viewrequests/', views.viewrequests, name='viewrequests'),
    path('acceptanddecryptfile/<int:id>/', views.acceptanddecryptfile, name='acceptanddecryptfile'),
    path('viewresponses/', views.viewresponses, name='viewresponses'),
    path('downloadfile/<int:id>/', views.downloadfile, name='downloadfile'),




   
]
