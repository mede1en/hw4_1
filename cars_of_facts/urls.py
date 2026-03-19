from django.urls import path
from .views import CarListView, CarDetailView, SearchView

app_name = 'mashiny'

urlpatterns = [
    path('car_list/', CarListView.as_view, name='car_list'),
    path('car_list/<int:id>/', CarDetailView.as_view, name='car_detail'),
    path('search/', SearchView.as_view, name='search'),

]