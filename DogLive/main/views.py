from django.http import HttpResponse
from django.shortcuts import render

menu = [{'title': "Главная", 'url_name': 'home/'},
        {'title': "Услуги", 'url_name': 'services/'},
        {'title': "Контакты", 'url_name': 'contacts/'},
        {'title': "О нас", 'url_name': 'about/'},
        {'title': "Войти", 'url_name': 'auth/'}]

def index(request):
    context = {'menu': menu,
               'title': "Главная"}
    return render(request, 'main/index.html', context = context)

def services(request):
    context = {'menu': menu,
               'title': "Услуги"}
    return render(request, 'main/services.html', context = context)

def contacts(request):
    context = {'menu': menu,
               'title': "Контакты"}
    return render(request, 'main/contacts.html', context = context)

def about(request):
    context = {'menu': menu,
               'title': "О нас"}
    return render(request, 'main/about.html', context = context)

def auth(request):
    return render(request, '')

def auth_id(request):
    return render(request, '')


def register(request):
    return render(request, '')

def record(request):
    return render(request, '')

def account(request):
    return render(request, '')