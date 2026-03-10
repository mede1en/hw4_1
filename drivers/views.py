from django.shortcuts import render, redirect, get_object_or_404
from drivers.models import DriverModel
from drivers.forms import DriverForm


#create
def create_driver_view(request):
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/drivers_list/')
    else: 
        form = DriverForm()
    return render(request, 'create_driver.html', {'form': form})


#read
def drivers_list_view(request):
    if request.method == 'GET':
        drivers = DriverModel.objects.all().order_by('-id')
    return render(request, 'drivers_list.html', {'drivers': drivers})

#update
def update_driver_view(request, id):
    driver = get_object_or_404(DriverModel, id=id)
    if request.method == 'POST':
        form = DriverForm(request.POST,  instance=driver)
        if form.is_valid():
            form.save()
            return redirect('/drivers_list/')
    else:
        form = DriverForm(instance=driver)
    return render(request, 'update_driver.html', {'form': form, 'driver': driver})


#delete
def delete_driver_view(request, id):
    driver = get_object_or_404(DriverModel, id=id)
    driver.delete()
    return redirect('/drivers_list/')