from django.shortcuts import render

def home(request):
    return render(request, 'dashboard/pages/home.html')

def about(request):
    return render(request, 'dashboard/pages/about.html')