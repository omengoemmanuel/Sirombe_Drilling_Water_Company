from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from admins.models import userprofile, survey_and_local_fee, Survey_Application

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .credentials import MpesaPpassword, MpesaAccessToken
import requests
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exist')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, 'Password did not match, please try again')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        # send_verification_email(user)

        messages.success(request, "Your Account has been created successfully")

        return redirect('signin')

    return render(request, 'signup.html')


def send_verification_email():
    subject = "Thank you for registering"
    message = f"Hi {User.first_name} \n\n Thank you for registering at our website. please verify your email to activate your account"
    recipient_list = [User.email]
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)


def p_photo(request):
    if request.method == "POST":
        profile_photos = request.POST.get('profile_photos')

        proffs = userprofile(profile_photos=profile_photos)
        proffs.save()
        messages.success(request, "Profile uploaded successfully")
        return redirect('user_profile')
    return redirect('user_profile')


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


@login_required
def welcome(request):
    email = request.user.email
    wel = User.objects.get(email=email)

    try:
        survey_application = Survey_Application.objects.get(Email_Address=email)
        status = survey_application.status
    except Survey_Application.DoesNotExist:
        status = "Verified"

    try:
        pic = userprofile.objects.get(email=email)
        picture = pic.p_photo
    except userprofile.DoesNotExist:
        picture = ''

    return render(request, 'adminweb/index.html', {'wel': wel, 'status': status, 'picture': picture})


def user_profile(request):
    fnane = request.user.first_name
    lname = request.user.last_name
    email = request.user.email
    proff = get_object_or_404(User, email=email)
    wel = User.objects.get(email=email)

    try:
        pic = userprofile.objects.get(email=email)
        picture = pic.p_photo
        fname = pic.fname
        lname = pic.lname
        company = pic.company
        job = pic.job
        county = pic.county
        address = pic.address
        phone = pic.phone
        email = pic.email
    except userprofile.DoesNotExist:
        pass

    return render(request, 'adminweb/users-profile.html',
                  {'navbar': 'user_profile', 'fname': fnane, 'lname': lname, 'proff1': proff, 'wel': wel, 'picture':picture, 'fname':fnane,'lname':lname,'company':company,'job':job,'county':county,'address':address,'phone':phone,'email':email })


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
        p_photo = request.FILES['p_photo']

        prof = userprofile(fname=fname, lname=lname, company=company, job=job, county=county,
                           address=address, phone=phone, email=email, p_photo=p_photo)
        prof.save()

    messages.success(request, 'Profile updated successfully')
    return redirect('user_profile')


def survey(request):
    email = request.user.email
    suv = get_object_or_404(userprofile, email=email)
    suv2 = get_object_or_404(survey_and_local_fee)
    wel = User.objects.get(email=email)

    try:
        pic = userprofile.objects.get(email=email)
        picture = pic.p_photo
    except userprofile.DoesNotExist:
        picture = ''

    return render(request, 'adminweb/survey.html', {'suv1': suv, 'suv3': suv2, 'wel': wel, 'picture': picture})


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


def pay(request):
    email = request.user.email
    pay2 = Survey_Application.objects.get(Email_Address=email)

    return render(request, 'adminweb/pay.html', {'pay2': pay2})


def stkpush(request):
    if request.method == 'POST':
        Mpesa_phone = request.POST['Mpesa_phone']
        Amount_paid = request.POST['Amount_paid']

        access_token = MpesaAccessToken.validated_access_token
        api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

        headers = {'Authorization': "Bearer %s" % access_token}

        request = {
            "BusinessShortCode": MpesaPpassword.short_code,
            "Password": MpesaPpassword.decoded,
            "Timestamp": MpesaPpassword.pay_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": Amount_paid,
            "PartyA": Mpesa_phone,
            "PartyB": MpesaPpassword.short_code,
            "PhoneNumber": Mpesa_phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Sirombe Springs Drilling Co.",
            "TransactionDesc": "Sirombe Springs Drilling Co. Survey charges"

        }
        response = requests.post(api_url, json=request, headers=headers)

    return HttpResponse("Payment sent successfully")


def layout(request):
    return render(request, 'adminweb/layout.html')
