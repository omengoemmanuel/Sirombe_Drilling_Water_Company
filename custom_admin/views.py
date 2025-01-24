from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from admins.models import userprofile, Survey_Application, drilling_and_pump_installation, Tank, Pump
from django.contrib.auth import get_user_model, logout
from django.contrib.admin.views.decorators import staff_member_required
from welcome.models import blog_page, messagess, booking
from django.contrib import messages


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
def update_admin_privilege(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        is_staff = request.POST.get('is_staff') == "on"

        try:
            user = User.objects.get(id=user_id)
            user.is_staff = is_staff
            user.save()
            messages.success(request, f"Admin privilege{'granted' if is_staff else 'revoked'} for {user.first_name}.")
        except User.DoesNotExist:
            messages.error(request, "User not found.")
        return redirect(request.META.get('HTTP_REFERER', "/"))


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


@staff_member_required
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


@staff_member_required
def survey_app(request):
    suv_app = Survey_Application.objects.all()
    return render(request, 'admincustom/surveyapplication.html', {'suv_app': suv_app})


def survey_app_del(request, id):
    suv_del = Survey_Application.objects.get(id=id)
    suv_del.delete()
    return redirect('survey_app')


@staff_member_required
def edit_survey_app(request, id):
    if request.method == 'POST':
        Survey_Category = request.POST.get('category')
        First_Name = request.POST.get('fname')
        Last_Name = request.POST.get('lname')
        Email_Address = request.POST.get('email')
        Phone_Number = request.POST.get('phone')
        Survey_Fee = request.POST.get('sfee')
        Local_Authority_Fee = request.POST.get('lfee')
        Total_Amount = request.POST.get('tamount')
        Amount_paid = request.POST.get('Amount_paid')
        depth = request.POST.get('depth')
        height = request.POST.get('height')
        status = request.POST.get('status')

        edit_surveys = Survey_Application.objects.get(id=id)
        edit_surveys.Survey_Category = Survey_Category
        edit_surveys.First_Name = First_Name
        edit_surveys.Last_Name = Last_Name
        edit_surveys.Email_Address = Email_Address
        edit_surveys.Phone_Number = Phone_Number
        edit_surveys.Survey_Fee = Survey_Fee
        edit_surveys.Local_Authority_Fee = Local_Authority_Fee
        edit_surveys.Total_Amount = Total_Amount
        edit_surveys.Amount_paid = Amount_paid
        edit_surveys.depth = depth
        edit_surveys.height = height
        edit_surveys.status = status

        edit_surveys.save()
        return redirect('survey_app')

    edit_surveys = Survey_Application.objects.get(id=id)
    return render(request, 'admincustom/edit_survey_app.html', {'edit_surveys': edit_surveys})


@staff_member_required()
def blog_update(request):
    blog_item = blog_page.objects.all()
    return render(request, 'admincustom/blog_update.html', {'blog_item': blog_item})


def blog_update_insert(request):
    if request.method == 'POST':
        blog_name = request.POST.get('blog_name')
        blog_description = request.POST.get('blog_description')
        date = request.POST.get('date')
        image = request.FILES['image']

        blogs_photos = blog_page(blog_name=blog_name, blog_description=blog_description, date=date, image=image)
        blogs_photos.save()
        messages.success(request, 'Blog photo added successfully')

        return redirect('blog_update')
    return redirect('blog_update')


def blog_update_delete(request, id):
    blog_del = blog_page.objects.get(id=id)
    blog_del.delete()
    messages.success(request, 'Blog deleted successfully')
    return redirect('blog_update')


def new_message(request):
    megg = messagess.objects.all()
    return render(request, 'admincustom/new_message.html', {'megg': megg})


def booking_made(request):
    book = booking.objects.all()
    return render(request, 'admincustom/bookings_made.html', {'book': book})


def tank(request):
    tnk = Tank.objects.all()
    return render(request, 'admincustom/tanks.html', {'tnk': tnk})


def add_tank(request):
    if request.method == 'POST':
        tank = request.POST.get('tank')
        cost = request.POST.get('cost')
        tank_photo = request.FILES['tank_photo']

        tank_save = Tank(tank=tank, cost=cost, tank_photo=tank_photo)
        tank_save.save()
        messages.success(request, 'Tank added successfully')

        return redirect('tank')
    return render(request, 'admincustom/add_tank.html')


def delete_tank(request, id):
    del_tank = Tank.objects.get(id=id)
    del_tank.delete()
    messages.success(request, 'Tank deleted successfully')
    return redirect('tank')


def edit_tank(request, id):
    if request.method == 'POST':
        tank = request.POST.get('tank')
        cost = request.POST.get('cost')
        tank_photo = request.FILES['tank_photo']

        edi = Tank.objects.get(id=id)
        edi.tank = tank
        edi.cost = cost
        edi.tank_photo = tank_photo
        edi.save()
        messages.success(request, 'Tank item updated successfully')
        return redirect('tank')

    edi = Tank.objects.get(id=id)
    return render(request, 'admincustom/edit tank.html', {'edi': edi})


def pump(request):
    pumpss = Pump.objects.all()
    return render(request, 'admincustom/pump.html', {'pumpss': pumpss})


def add_pump(request):
    if request.method == 'POST':
        pump = request.POST.get('pump')
        cost = request.POST.get('cost')
        pump_photo = request.FILES['pump_photo']

        ad_pump = Pump(pump=pump, cost=cost, pump_photo=pump_photo)
        ad_pump.save()
        messages.success(request, "Pump added successfully")
        return redirect('pump')
    return render(request, 'admincustom/add_pump.html')


def delete_pump(request, id):
    del_pump = Pump.objects.get(id=id)
    del_pump.delete()
    messages.success(request, "Pump details deleted successfully")
    return redirect('pump')


def edit_pump(request, id):
    if request.method == 'POST':
        pump = request.POST.get('pump')
        cost = request.POST.get('cost')
        pump_photo = request.FILES['pump_photo']

        edi_pump = Pump.objects.get(id=id)
        edi_pump.pump = pump
        edi_pump.cost = cost
        edi_pump.pump_photo = pump_photo
        edi_pump.save()
        messages.success(request, "Pump edited successfully")
        return redirect('pump')

    ed_pump = Pump.objects.get(id=id)
    return render(request, 'admincustom/edit_pump.html', {'ed_pump': ed_pump})
