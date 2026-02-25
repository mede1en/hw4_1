from django.urls import path
from .views import Kiafacts_view, BMWfacts_view, Toyotafacts_view

urlpatterns = [
    path('kiafacts/', Kiafacts_view),
    path('bmwfacts/', BMWfacts_view),
    path('toyotafacts/', Toyotafacts_view),
]