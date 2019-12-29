from django.shortcuts import render

def index(request):
    context = {}
    template = 'index.html'
    return render(request, template, context)

def user_login(request):
    context = {}
    template = 'login-register.html'
    return render(request, template, context)

def register(request):
    context = {}
    template = 'login-register.html'
    return render(request, template, context)
