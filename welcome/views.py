from django.shortcuts import render, redirect
from welcome.models import blog_page, messagess, booking
from admins.models import survey
from django.contrib import messages


# Create your views here.
def index(request):
    price1 = survey.objects.all()
    return render(request, 'index.html', {'navbar': 'index', 'price1': price1})


def about(request):
    return render(request, 'about.html', {'navbar': 'about', })


def service(request):
    return render(request, 'service.html', {'navbar': 'service', })


def blog(request):
    blog1 = blog_page.objects.all()
    return render(request, 'blog.html', {'navbar': 'blog', 'blog1': blog1})


def contact(request):
    return render(request, 'contact.html', {'navbar': 'contact'})


def messageinsert(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        mess = messagess(fname=fname, lname=lname, phone=phone, mail=mail, subject=subject, message=message)
        mess.save()
        messages.success(request, "Message sent successfully")

        return redirect('/contact')
    return redirect('/contact')


def bookings(request):
    if request.method == "POST":
        query_type = request.POST.get('query_type')
        location = request.POST.get('location')
        pick_date = request.POST.get('pick_date')
        pick_time = request.POST.get('pick_time')
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        book = booking(query_type=query_type, location=location, pick_date=pick_date, pick_time=pick_time, name=name,
                       phone=phone)
        book.save()

        return redirect('/')
    return redirect('/')
