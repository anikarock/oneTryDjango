from django.shortcuts import render


# Create your views here.

def index(request):
    data={
        'title': 'Главная страничка',
        'values':['Hi','Some','75']
    }
    return render(request,'main/index.html',data)

def about(request):
    return render(request,'main/about.html')
 