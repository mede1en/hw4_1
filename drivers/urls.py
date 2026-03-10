from django.urls import path
from drivers.views import create_driver_view, drivers_list_view, update_driver_view, delete_driver_view

urlpatterns = [
    path('create_driver/', create_driver_view, name='create_driver'),
    path('drivers_list/', drivers_list_view),
    path('drivers_list/<int:id>/update/', update_driver_view),
    path('drivers_list/<int:id>/delete/', delete_driver_view),
]