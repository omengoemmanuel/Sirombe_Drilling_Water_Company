from django.shortcuts import render, redirect
from .models import survey
from admins.models import userprofile, survey_and_local_fee

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your Account has been created successfully")

        return redirect('signin')

    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect("welcome")
        else:
            messages.error(request, "Invalid Logins")
            return redirect("signin")

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect("signin")


def home(request):
    fnane = request.user.first_name
    lname = request.user.last_name
    return render(request, 'home.html', {'navbar': 'home', 'fname': fnane, 'lname': lname})


def welcome(request):
    return render(request, 'adminweb/index.html')


def user_profile(request):
    fnane = request.user.first_name
    lname = request.user.last_name
    email = request.user.email
    pro1 = userprofile.objects.all()

    return render(request, 'adminweb/users-profile.html',
                  {'navbar': 'user_profile', 'fname': fnane, 'lname': lname, 'email': email, 'pro1': pro1})


def profileinsert(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        company = request.POST.get('company')
        job = request.POST.get('job')
        county = request.POST.get('county')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        prof = userprofile(fname=fname, lname=lname, company=company, job=job, county=county,
                           address=address, phone=phone, email=email)
        prof.save()

        messages.success(request, 'Profile updated successfully')
        return redirect('user_profile')
    return redirect('user_profile')


def survey(request):
    prof = userprofile.objects.all().values_list('fname')
    suv = survey_and_local_fee.objects.all()

    return render(request, 'adminweb/survey.html', {'suv': suv, 'prof': prof})
