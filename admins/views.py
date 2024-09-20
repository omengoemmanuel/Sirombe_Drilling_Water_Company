from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import survey
from admins.models import userprofile, survey_and_local_fee, Survey_Application, profile_photo

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
    email = request.user.email
    wel = User.objects.get(email=email)
    return render(request, 'adminweb/index.html', {'wel': wel})


def user_profile(request):
    fnane = request.user.first_name
    lname = request.user.last_name
    email = request.user.email
    proff = get_object_or_404(User, email=email)
    wel = User.objects.get(email=email)

    return render(request, 'adminweb/users-profile.html',
                  {'navbar': 'user_profile', 'fname': fnane, 'lname': lname, 'proff1': proff, 'wel': wel})


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
                           address=address, phone=phone, email=email, )
        prof.save()

        messages.success(request, 'Profile updated successfully')
        return redirect('user_profile')
    return redirect('user_profile')


def survey(request):
    email = request.user.email
    suv = get_object_or_404(userprofile, email=email)
    suv2 = get_object_or_404(survey_and_local_fee)
    wel = User.objects.get(email=email)

    return render(request, 'adminweb/survey.html', {'suv1': suv, 'suv3': suv2, 'wel': wel})


def Survey_Application_insert(request):
    if request.method == 'POST':
        Survey_Category = request.POST.get('category')
        First_Name = request.POST.get('fname')
        Last_Name = request.POST.get('lname')
        Email_Address = request.POST.get('email')
        Phone_Number = request.POST.get('phone')
        Survey_Fee = request.POST.get('sfee')
        Local_Authority_Fee = request.POST.get('lfee')
        Total_Amount = request.POST.get('tamount')

        application = Survey_Application(Survey_Category=Survey_Category, First_Name=First_Name, Last_Name=Last_Name,
                                         Email_Address=Email_Address, Phone_Number=Phone_Number, Survey_Fee=Survey_Fee,
                                         Local_Authority_Fee=Local_Authority_Fee, Total_Amount=Total_Amount)
        application.save()
        messages.success(request, 'Survey application sent successfully')
        return redirect('pay')
    return redirect('pay')


def Survey_Application_commercial_insert(request):
    if request.method == 'POST':
        Survey_Category = request.POST.get('cat')
        First_Name = request.POST.get('f_name')
        Last_Name = request.POST.get('l_name')
        Email_Address = request.POST.get('email')
        Phone_Number = request.POST.get('phone')
        Survey_Fee = request.POST.get('s_fee')
        Local_Authority_Fee = request.POST.get('l_fee')
        Total_Amount = request.POST.get('t_amount')

        application = Survey_Application(Survey_Category=Survey_Category, First_Name=First_Name, Last_Name=Last_Name,
                                         Email_Address=Email_Address, Phone_Number=Phone_Number, Survey_Fee=Survey_Fee,
                                         Local_Authority_Fee=Local_Authority_Fee, Total_Amount=Total_Amount)
        application.save()
        messages.success(request, 'Survey application sent successfully')
        return redirect('pay')


def pay(request):
    email = request.user.email
    pay2 = Survey_Application.objects.get(Email_Address=email)

    return render(request, 'adminweb/pay.html', {'pay2': pay2})


def p_photo(request):
    if request.method == 'POST':
        profile_photos = request.FILES['profile_photos']
        pphoto = profile_photo(profile_photos = profile_photos)
        pphoto.save()
        return redirect('user_profile')

