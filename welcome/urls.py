from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('service', views.service),
    path('blog', views.blog),
    path('contact', views.contact),
    path('messageinsert', views.messageinsert),


]
