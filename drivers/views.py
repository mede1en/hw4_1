from django.shortcuts import render, redirect, get_object_or_404
from drivers.models import DriverModel
from drivers.forms import DriverForm
from django.views import generic



class CreateDriverView(generic.CreateView):
    template_name = 'create_driver.html'
    form_class = DriverForm
    success_url = '/drivers_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateDriverView, self).form_valid(form=form)

class DriverListView(generic.ListView):
    template_name = 'drivers_list.html'
    model = DriverModel
    context_object_name = 'drivers'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class UpdateDriverView(generic.UpdateView):
    template_name = 'update_driver.html'
    form_class = DriverForm
    model = DriverModel
    success_url = '/drivers_list/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=order_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateDriverView, self).form_valid(form=form)


class DeleteDriverView(generic.View):
    def get(self, request, id):
        order_id = get_object_or_404(DriverModel, id=id)
        order_id.delete()
        return redirect('/drivers_list/')
