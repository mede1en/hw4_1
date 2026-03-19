from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator
from django.db.models import F 
from django.views import generic


class SearchView(generic.ListView):
    template_name = 'car_list.html'
    context_object_name = 'car_key'
    model = Car

    def get_queryset(self):
        return self.model.objects.filter(name_book__icontains=self.request.GET.get('s'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context


class CarListView(generic.ListView):
    template_name = 'car_list.html'
    model = Car
    context_object_name = 'car_key'
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_key'] = context['page_obj']
        return context

class CarDetailView(generic.DetailView):
    template_name = 'car_detail.html'
    context_object_name = 'car_id_key'
    pk_url_kwarg = 'id'
    model = Car

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request
    
        views_car = request.session.get('viewed_car', [])

        if obj.pk not in views_car:
            Car.objects.filter(pk=obj.pk).update(
                views = F("views")+1
                )
            views_car.append(obj.pk)
            request.session['views_car'] = views_car

            obj.refresh_from_db()
        return obj
    
