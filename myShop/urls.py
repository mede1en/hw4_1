from django.urls import path
from myShop.views import categories_view, products_view, category_products_view

urlpatterns = [
    path('categories/', categories_view),
    path('products/', products_view),
    path('category/<int:category_id>/', category_products_view)
]