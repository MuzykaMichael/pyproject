from django.shortcuts import render

db = [
{'author': 'MMO', 'title': 'zxc', 'content': 'zxzsd', 'date_added': '2023' , 'link':'https://docs.djangoproject.com/en/5.0/ref/urls/', 'short_desc':''},
{'author': 'MMzxcO', 'title': 'zxrr', 'content': 'zxzsw', 'date_added': '2024' , 'link':'https://docs.djangoproject.com/en/5.0/ref/urls/', 'short_desc':''}
]



def home(request):
    context = {
        "projects": db,
    }
    return render(request, 'blog/home.html', context)

def contact(request):
    return render(request, 'blog/contact.html')

def projects(request):
    return render(request, 'blog/projects.html')


