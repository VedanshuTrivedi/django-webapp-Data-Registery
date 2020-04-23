from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserRegisterForm
from django.views.generic.edit import CreateView ,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# from .forms import ItemForm
from .models import Item 

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import ItemForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to login ')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ItemForm()

    return render(request, 'home.html', {'form': form})

# def itemview(request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form' : form
#     }
#     return render(request,'myapp/home.html',context)

class itemview(CreateView): 
    # specify the model for create view 
    model = Item 
    #specify the fields to be displayed 
    fields = [	'id','detail1','detail2','detail3','material','gauge','quantity',	'rate',	'size',	'colour','podetail','process','billdetail','stock']
    template_name='home.html'

class itemupdateview(UpdateView): 
    # specify the model for create view 
    model = Item 
    # specify the fields to be displayed 
    fields = ['id','detail1','detail2','detail3','material','gauge','quantity',	'rate',	'size',	'colour','podetail','process','billdetail','stock']
    template_name='home.html'

class itemdeleteview(DeleteView): 
    # specify the model for create view 
    model = Item 
    # specify the fields to be displayed 
    fields = ['id','detail1','detail2','detail3','material','gauge','quantity',	'rate',	'size',	'colour','podetail','process','billdetail','stock']
    template_name='home.html'

class ItemDetailView(DetailView): 
    # specify the model for create view 
    model = Item 
    #specify the fields to be displayed 
    fields = [	'id','detail1','detail2','detail3','material','gauge','quantity',	'rate',	'size',	'colour','podetail','process','billdetail','stock']
    template_name='detail.html'


class itemlistview(ListView): 
    # specify the model for create view 
    model = Item 
    #specify the fields to be displayed 
    fields = [	'id','detail1','detail2','detail3','material','gauge','quantity',	'rate',	'size',	'colour','podetail','process','billdetail','stock']
    template_name='list.html'

# Create your views here.
# def homepageview(request):
#     return render(request,'home.html',{'name':'Trivedi'})


# def contactpageview(request):
#     return HttpResponse('welcome to contact ')
