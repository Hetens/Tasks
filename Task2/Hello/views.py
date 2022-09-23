from curses.ascii import HT
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
ans ={}

def greet(request,n,q):
    temp =int(1)
    k =0
    for j in range(n,q):
        beq =[]
        temp =j
        while temp != 0:
            beq.append(temp%2)
            temp =temp //2
        for k in range(len(beq)-1):
            if beq[k] ==1 and beq[k+1] ==1:
                ans[j] ='True'
            else:
                ans[j] ='False'    
    return JsonResponse(ans)
    
