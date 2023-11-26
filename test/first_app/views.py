from django.shortcuts import render

def home(request):
    return render(request, 'landing/home.html')

def about(request):
    return render(request, 'landing/about.html')

def contacts(request):
    return render(request, 'landing/contacts.html')
