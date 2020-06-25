from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'gen/index.html')


def wordpass(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    p = ''

    if(request.GET.get('uppercase')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if(request.GET.get('special')):
        characters.extend(list('!@#$%^&*()'))

    if(request.GET.get('digits')):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))

    for i in range(length):
        p += random.choice(characters)

    return render(request, 'gen/wordpass.html', {'password': p})
