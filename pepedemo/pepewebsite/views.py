from django.shortcuts import render

# Create your views here.

posts =[
    {'author':'pepe',
     'title': 'Avi',
     'content': 'website application',
     'date_posted': 'march 15, 2020'
     },
    {'author': 'johnspelling',
     'title': 'myapp',
     'content': 'website application',
     'date_posted': 'september 12, 2020'
     }

]
def home(request):
    context={'posts': posts
             }
    return render(request, 'pepewebsite/home.html',context)

def profile(request):
    return render(request, 'pepewebsite/profile.html')