
from django.shortcuts import render
import requests
from .forms import Queryform
from django.http import HttpResponseRedirect


# Create your views here.
queries =['Which song is this']
def index(request):
    return render(request, 'queryform/index.html', {'queries':queries})

def question(request):
    if request.method =='POST':
        form =Queryform(request.POST)
        if form.is_valid():#cleaned_data is only invoked after the isvalid check
            query = form.cleaned_data["query"]
            queries.append(query)
        else:
            return render(request, 'queryform/Form.html',{"form": form})#returns the existing form data
    return render(request, 'queryform/Form.html', {"form":Queryform()} )