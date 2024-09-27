from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('service', views.service),
    path('blog', views.blog),
    path('contact', views.contact),
    path('messageinsert', views.messageinsert),
    path('bookings', views.bookings, name='bookings'),
]
