from django.shortcuts import render
import requests
# from .forms import PDFFileForm

mainprojects = [
{'author': 'MMO', 'title': 'zxc', 'content': 'zxzsd', 'date_added': '2023' , 'link':'https://docs.djangoproject.com/en/5.0/ref/urls/', 'short_desc':''},
{'author': 'MMzxcO', 'title': 'zxrr', 'content': 'zxzsw', 'date_added': '2024' , 'link':'https://docs.djangoproject.com/en/5.0/ref/urls/', 'short_desc':''}
]

about = {
    'title': 'My Contacts',
    'phone': '+380500356268',
    'email': 'm.muzyka.mailbox@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/mykhailo-muzyka1/',
    'github': 'https://github.com/MuzykaMichael',
    'TG': 'https://t.me/batich_v_zdanii',
}



def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    context = {
        'contact': about
    }
    return render(request, 'blog/contact.html', context)

def projects(request):
    context = {
        "projects": mainprojects,
    }
    return render(request, 'blog/projects.html', context)

def currencyapi(request):
    r = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=c80bb83b35a335d5c2e6b281107fca10').json()
    res = r['rates']
    context = {
        'rates': res.items(),
        'title': 'Currency API Page'
    }
    return render(request, 'blog/currencyapi.html', context)

# def uploadpdf(request):
#     if request.method == 'POST':
#         form = PDFFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#         else:
#             form = PDFFileForm()
#             return render(request, 'upload.html', {'form': form})
#

