from django.shortcuts import render
import requests

db = [
{'author': 'MMO', 'title': 'zxc', 'content': 'zxzsd', 'date_added': '2023' , 'link':'https://docs.djangoproject.com/en/5.0/ref/urls/', 'short_desc':''},
{'author': 'MMzxcO', 'title': 'zxrr', 'content': 'zxzsw', 'date_added': '2024' , 'link':'https://docs.djangoproject.com/en/5.0/ref/urls/', 'short_desc':''}
]



def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    return render(request, 'blog/contact.html')

def projects(request):
    context = {
        "projects": db,
    }
    return render(request, 'blog/projects.html', context)

def currencyapi(request):
    r = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=c80bb83b35a335d5c2e6b281107fca10').json()
    res = r['rates']
    context = {
        'rates': res.items(),
    }
    return render(request, 'blog/currencyapi.html', context)


