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

]
