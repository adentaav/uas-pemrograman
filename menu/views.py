from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'banner1': 'img\menu0.jpg',
        'gng1' : 'img/gng1.jpg',
        'gng2' : 'img/gng2.jpg',
        'gng3' : 'img/gng3.jpg',
        'gng4' : 'img/gng4.jpg',
        'nav1': [
            ['/', 'Home'],
            ['/menu', 'Menu']
        ]
    }
    return render(request, 'menu.html', context)