from django.shortcuts import render, get_object_or_404
from .models import Car
from django.http import HttpResponse


def Kiafacts_view(request):
    if request.method == 'GET':
        return HttpResponse('Kia made in South Korea')

def BMWfacts_view(request):
    if request.method == 'GET':
        return HttpResponse('BMW made in Germany ✨❤️')
    
def Toyotafacts_view(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://scene7.toyota.eu/is/image/toyotaeurope/toy_cor19_tpo_brandpriimgatlsdfront-2:Large-Landscape?' \
        'ts=1769976838098&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=png-alpha" >')



def car_list_view(req):
    if req.method == 'GET':
        cars = Car.objects.all().order_by('-id')
        return render(req, 'car_list.html', {'car_key': cars})
    


def car_detail_view(req,id):
    if req.method == 'GET':
        car_id = get_object_or_404(Car, id=id)
        return render(req, 'car_detail.html', {'car_id_key': car_id})