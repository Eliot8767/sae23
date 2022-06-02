from django.urls import path
from .import views
from computermngt import computerApp
urlpatterns = [
    path ('',views.index, name ='index') ,
    path ('machines/',
    views.machine_list_view ,
    name ='machines') ,
    path ('machine/<pk>',
    views.machine_detail_view,
    name ='machine-detail'),
    path('',views.about, name='about') ,
]