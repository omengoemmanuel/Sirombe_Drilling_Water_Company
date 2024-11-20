from django.shortcuts import render, HttpResponse
from admins.models import userprofile, Survey_Application, drilling_and_pump_installation
from django.contrib.auth import get_user_model


# Create your views here.
def custo(request):
    no = Survey_Application.objects.count()
    no_drill = drilling_and_pump_installation.objects.count()
    return render(request, 'admincustom/index.html', {'no': no, 'no_drill':no_drill})


def user_logins(request):
    User = get_user_model()
    logs = User.objects.all()
    return render(request, 'admincustom/userlogins.html', {'logs': logs})


def users_profile(request):
    users = userprofile.objects.all()
    return render(request, 'admincustom/userprofile.html', {'users': users})
