from django.shortcuts import render
from content_gen import views
from menu import menu_items
def index(request):
    return render(request, 'home_page/index.html', {
        'menu':menu_items,
    })

def about(request):
    return render(request, 'home_page/about.html', {
        'menu':menu_items,
    })

def login(request):
    return render(request, 'home_page/login.html', {
        'menu':menu_items
    })
    
