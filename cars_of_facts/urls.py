from django.urls import path
from .views import car_list_view, car_detail_view, search_view

app_name = 'mashiny'

urlpatterns = [
    path('car_list/', car_list_view, name='car_list'),
    path('car_list/<int:id>/', car_detail_view, name='car_detail'),
    path('search/', search_view, name='search'),

]