from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name ="index"),
    path('/yourquery',views.your_query, name ='your_query')
]