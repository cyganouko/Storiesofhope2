from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def donate(request):
    return render(request, 'donate.html')

def info(request):
    return render(request, 'info.html')

def about(request):
    return render(request, 'about.html')

def stories(request):
    return render(request, 'stories.html')

def events(request):
    return render(request, 'events.html')

def moreaboutus(request):
    return render(request, 'moreaboutus.html')
