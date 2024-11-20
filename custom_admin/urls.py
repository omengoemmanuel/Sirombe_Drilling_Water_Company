from django.urls import path
from . import views

urlpatterns = [
    path('custo', views.custo, name='custo'),
    path('user_logins', views.user_logins, name='user_logins'),
    path('users_profile', views.users_profile, name='users_profile')
]
