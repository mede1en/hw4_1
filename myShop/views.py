from django.shortcuts import render, get_object_or_404
from myShop.models import Category, Product


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories_key': categories})


def products_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products_key': products})


def category_products_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    return render(request, 'category_products.html', {
        'category': category,
        'products': products
    })