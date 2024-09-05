from django.shortcuts import render
from .models import survey


# Create your views here.
def signup(request):
    return render(request, 'signup.html')


def signin(request):
    pass


def signout(request):
    pass
