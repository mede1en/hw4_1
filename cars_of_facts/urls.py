from django.urls import path
from .views import car_list_view, car_detail_view

urlpatterns = [
    path('car_list/', car_list_view),
    path('car_list/<int:id>/', car_detail_view),
]