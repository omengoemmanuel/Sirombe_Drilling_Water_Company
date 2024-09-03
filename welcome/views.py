from django.shortcuts import render
from admins.models import survey


# Create your views here.
def index(request):
    price1 = survey.objects.all()
    return render(request, 'index.html', {'navbar': 'index', 'price1': price1})


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')
