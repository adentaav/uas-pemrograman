from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    context = {
        'banner': 'img/foto.jpg',
        'nav': [
            ['/', 'Home'],
            ['/menu', 'Menu']
        ]
    }
    return render (request, 'base.html', context)
