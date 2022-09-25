from urllib import response
from django.shortcuts import render
import requests
from .forms import Queryform
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'queryform/Form.html')

def get_query(request):
    if request.method == 'POST':
        form = Queryform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            return HttpResponseRedirect('/yourquery')
        else:
            form = Queryform()#creates a blank form
            return render(request, 'Form.html',{'form':form})

def your_query(request):
    return HttpResponseRedirect(redirect_to='/queryform')