from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.auth_logout_view, name='logout'),
    path('congratulation/', views.cong_view, name='congratulation'),
]