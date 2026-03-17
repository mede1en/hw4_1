from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator
from django.db.models import F 


def search_view(request):
    query = request.GET.get("s", "")
    if query:
        cars = Car.objects.filter(name__icontains=query)
    else:
        cars = Car.objects.none()
    return render(
        request,
        'car_list.html',
        {'car_key': cars}
    )


# def Kiafacts_view(request):
#     if request.method == 'GET':
#         return HttpResponse('Kia made in South Korea')

# def BMWfacts_view(request):
#     if request.method == 'GET':
#         return HttpResponse('BMW made in Germany ✨❤️')
    
# def Toyotafacts_view(request):
#     if request.method == 'GET':
#         return HttpResponse('<img src="https://scene7.toyota.eu/is/image/toyotaeurope/toy_cor19_tpo_brandpriimgatlsdfront-2:Large-Landscape?' \
#         'ts=1769976838098&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=png-alpha" >')



def car_list_view(req):
    if req.method == 'GET':
        cars = Car.objects.all().order_by('-id')
        paginator = Paginator(cars, 2) 
        page = req.GET.get('page')
        page_obj = paginator.get_page(page)

        return render(
            req, 
            'car_list.html', 
            {
                'car_key': page_obj
            }
        )
    


def car_detail_view(req, id):
    car_id = get_object_or_404(Car, id=id)
    views_car = req.session.get('viewed_car', [])

    if id not in views_car:

        car_id.views = F('views') + 1
        car_id.save()
        car_id.refresh_from_db()

        views_car.append(id)   
        req.session['viewed_car'] = views_car
        req.session.modified = True

    return render(
        req,
        'car_detail.html',
        {
            'car_id_key': car_id
        }
    )