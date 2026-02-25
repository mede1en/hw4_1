from django.shortcuts import render
from django.http import HttpResponse

def Kiafacts_view(request):
    if request.method == 'GET':
        return HttpResponse('Kia made in South Korea')

def BMWfacts_view(request):
    if request.method == 'GET':
        return HttpResponse('BMW made in Germany ✨❤️')
    
def Toyotafacts_view(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://scene7.toyota.eu/is/image/toyotaeurope/toy_cor19_tpo_brandpriimgatlsdfront-2:Large-Landscape?ts=1769976838098&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=png-alpha" >') 
