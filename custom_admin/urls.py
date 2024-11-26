from django.urls import path
from . import views

urlpatterns = [
    path('custo', views.custo, name='custo'),
    path('user_logins', views.user_logins, name='user_logins'),
    path('users_profile', views.users_profile, name='users_profile'),
    path('log_out', views.log_out, name='log_out'),
    path('delete_user/<id>', views.delete_user, name='delete_user'),
    path('delete_profile/<id>', views.delete_profile, name='delete_profile'),
    path('edit_user_profile/<id>', views.edit_user_profile, name='edit_user_profile'),
    path('survey_app', views.survey_app, name='survey_app'),
    path('survey_app_del/<id>', views.survey_app_del, name='survey_app_del'),
    path('edit_survey_app', views.edit_survey_app, name='edit_survey_app'),
    path('edit_survey_app/<id>', views.edit_survey_app, name='edit_survey_app'),
    path('blog_update', views.blog_update, name='blog_update'),
    path('blog_update_insert', views.blog_update_insert, name='blog_update_insert'),
    path('blog_update_delete/<id>', views.blog_update_delete, name='blog_update_delete'),
    path('new_message', views.new_message, name='new_message'),
    path('booking_made', views.booking_made, name='booking_made'),
    path('tank', views.tank, name='tank'),
    path('add_tank', views.add_tank, name='add_tank'),
    path('delete_tank/<id>', views.delete_tank, name='delete_tank'),
    path('edit_tank/<id>', views.edit_tank, name='edit_tank')

]
