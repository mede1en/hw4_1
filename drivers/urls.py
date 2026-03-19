from django.urls import path
from drivers.views import CreateDriverView, DriverListView, UpdateDriverView, DeleteDriverView

urlpatterns = [
    path('create_driver/', CreateDriverView.as_view, name='create_driver'),
    path('drivers_list/', DriverListView.as_view),
    path('drivers_list/<int:id>/update/', UpdateDriverView.as_view),
    path('drivers_list/<int:id>/delete/', DeleteDriverView.as_view),
]