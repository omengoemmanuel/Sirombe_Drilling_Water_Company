from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
    path('home', views.home, name="home"),
    path('welcome', views.welcome, name="welcome"),
    path('user_profile', views.user_profile, name="user_profile"),
    path('profileinsert', views.profileinsert, name='profileinsert'),
    path('survey', views.survey, name='survey'),
    path('Survey_Application_insert', views.Survey_Application_insert, name='Survey_Application_insert'),
    path('pay', views.pay, name='pay'),
    path('stkpush', views.stkpush, name='stkpush'),
    path('p_photo', views.p_photo, name='p_photo'),
    path('layout', views.layout, name='layout'),
    path('change_password', views.change_password, name='change_password'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),

    path('drilling', views.drilling, name='drilling'),
    path('get-downpayment/', views.get_downpayment, name='get_downpayment'),
    path('get-pump/', views.get_pump, name='get_pump'),
    path('get-tank/', views.get_tank, name='get_tank'),
    path('invoice', views.invoice, name='invoice')

]
