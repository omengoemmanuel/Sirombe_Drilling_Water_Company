from django.shortcuts import render
from welcome.models import blog_page
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
    blog1 = blog_page.objects.all()
    return render(request, 'blog.html', {'navbar': 'blog', 'blog1': blog1})


def contact(request):
    return render(request, 'contact.html')
