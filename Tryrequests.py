
import requests


response = requests.get('http://api.open-notify.org/astros.json',params = {'craft' :'ISS'})

print(response.json())