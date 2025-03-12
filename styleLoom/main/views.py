from django.shortcuts import render, get_object_or_404, redirect
# from .forms import ProductForm
from .models import Clothes


def home(request):
    return render(request, 'home.html')

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
    return render(request, 'product_detail.html', {'product': product})