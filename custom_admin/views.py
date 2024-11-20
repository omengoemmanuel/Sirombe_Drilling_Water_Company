from django.shortcuts import render, HttpResponse, redirect
from admins.models import userprofile, Survey_Application, drilling_and_pump_installation
from django.contrib.auth import get_user_model, logout
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
@staff_member_required()
def custo(request):
    no = Survey_Application.objects.count()
    no_drill = drilling_and_pump_installation.objects.count()
    User1 = get_user_model()
    adm = User1.objects.all()
    return render(request, 'admincustom/index.html', {'no': no, 'no_drill': no_drill, 'adm': adm})


def log_out(request):
    logout(request)
    return redirect("signin")


@staff_member_required()
def user_logins(request):
    User = get_user_model()
    logs = User.objects.all()
    return render(request, 'admincustom/userlogins.html', {'logs': logs})


@staff_member_required()
def users_profile(request):
    users = userprofile.objects.all()

    return render(request, 'admincustom/userprofile.html', {'users': users})


def delete_user(request, id):
    dele = get_user_model()
    delet = dele.objects.get(id=id)
    delet.delete()
    return redirect('user_logins')


def delete_profile(request, id):
    det_prof = userprofile.objects.get(id=id)
    det_prof.delete()
    return redirect("users_profile")


def edit_user_profile(request, id):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        company = request.POST.get('company')
        job = request.POST.get('job')
        county = request.POST.get('county')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        p_photo = request.FILES['p_photo']

        user_pro = userprofile.objects.get(id=id)

        user_pro.fname = fname
        user_pro.lname = lname
        user_pro.company = company
        user_pro.job = job
        user_pro.county = county
        user_pro.address = address
        user_pro.phone = phone
        user_pro.email = email
        user_pro.p_photo = p_photo
        user_pro.save()
        return redirect('users_profile')

    user_pro = userprofile.objects.get(id=id)
    return render(request, 'admincustom/edituserprof.html', {'user_pro': user_pro})
