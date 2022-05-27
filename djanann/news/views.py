
from django.shortcuts import redirect, render
from.models import Articels
from.forms import ArticelsForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news=Articels.objects.order_by('date')
    return render(request,'news/news_home.html',{'news':news})

class NewsDetail(DetailView):
    model=Articels
    template_name= 'news/detals.html'
    context_object_name='Articels'

class NewsUpdate(UpdateView):
    model=Articels
    template_name= 'news/create.html'
    form_class=ArticelsForm

class NewsDelete(DeleteView):
    model=Articels
    template_name= 'news/delete.html'
    success_url='/news/'


def create(request):
    error=''
    form=ArticelsForm()
    if request.method=='POST':
        form=ArticelsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error='форма не правильно указана'
    data= {
        'form': form,
        'error':error
    }

    return render(request,'news/create.html',data)
    
    