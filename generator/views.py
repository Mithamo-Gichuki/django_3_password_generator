from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password': 'qwerty1234'})


def landing(request):
    return HttpResponse('This is landing page')


def password(request):
    password_len = 10
    gen_pass = ''
    chars = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIGKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*~?/'))
    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))

    for x in range(password_len):
        gen_pass += random.choice(chars)
    return render(request, 'generator/password.html', {'password': gen_pass})


def about(request):
    return render(request, 'generator/about.html')
