from django.urls import path
from . import views

urlpatterns = [
    path('custo', views.custo, name='custo'),
    path('user_logins', views.user_logins, name='user_logins'),
    path('users_profile', views.users_profile, name='users_profile'),
    path('log_out', views.log_out, name='log_out'),
    path('delete_user/<id>', views.delete_user, name='delete_user'),
    path('delete_profile/<id>', views.delete_profile, name='delete_profile'),
    path('edit_user_profile/<id>', views.edit_user_profile, name='edit_user_profile')
]
