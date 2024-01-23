from django.shortcuts import render
from django.http import HttpResponse
from . import templates
def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    return render(request, 'blog/contact.html')

def projects(request):
    return render(request, 'blog/projects.html')


