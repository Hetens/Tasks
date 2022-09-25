
from asyncio.windows_events import NULL
from django.shortcuts import render
import requests
from .forms import Queryform
from django.http import HttpResponse





answer =[]
# Create your views here.
def index(request):
    return render(request, 'queryform/index.html', {'queries':answer})

def question(request):
    url = "https://spotify23.p.rapidapi.com/search/"

    

    headers = {
	"X-RapidAPI-Key": "3064e93a75msh4290adb8a28fe61p1a8456jsn4ac87731a7a1",
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }
    
    if request.method =='POST':
        form =Queryform(request.POST)
        if form.is_valid():#cleaned_data is only invoked after the isvalid check
            query = form.cleaned_data["query"]
            queries = query
            querystring = {"q":queries,"type":"multi","offset":"0","limit":"10","numberOfTopResults":"5"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            r = response.json()
            return render(request,'queryform/index.html',{'queries':r['tracks']['items']})
        else:
            return render(request, 'queryform/Form.html',{"form": form})#returns the existing form data
    return render(request, 'queryform/Form.html', {"form":Queryform()} )