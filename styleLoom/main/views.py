from django.shortcuts import render, get_object_or_404
from .models import Clothes


def home(request):
    products = Clothes.objects.all()
    return render(request, 'home.html', {'products': products})


def contact(request):
    return render(request, 'contact.html')


def products(request):
    gender_filter = request.GET.get('gender', 'all')

    if gender_filter == 'all':
        products = Clothes.objects.all()
    else:
        products = Clothes.objects.filter(gender=gender_filter)

    return render(request, 'products.html', {'products': products, 'gender_filter': gender_filter})


def product_detail(request, id):
    product = get_object_or_404(Clothes, id=id)
    related_products = Clothes.objects.filter(gender=product.gender).exclude(
        id=product.id)[:4] 

    return render(request, 'product_detail.html', {
        'product': product,
        'related_products': related_products 
    })
