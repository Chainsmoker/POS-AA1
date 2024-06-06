import stripe
from django.shortcuts import render, redirect
from .models import Productos

stripe.api_key = 'sk_test_51PO69TH4Ppt0zy152ViqB4prrYFJoxicD5L3mUrNQt3azPG1Q5KsriYuNVG4x2lAjE5T5FOxvK9eTTa2VVfgjVv100xJkMXNuk'

def shop(request):
    q = request.GET.get('search')
    if q:
        try:
            productos = Productos.objects.filter(nombre__icontains=request.GET.get('search'))
        except:
            productos = None

        context = {
            'productos': productos,
            'query': q
        }

        return render(request, 'search.html', context)
    else:
        productos = Productos.objects.all()
        context = {
            'productos': productos,
            'title': 'Shop | Uomo'
        }

        return render(request, 'shop/shop.html', context)

def product_detail(request, slug=None):
    try:
        product = Productos.objects.get(slug=slug)
    except Productos.DoesNotExist:
        product = None

    context = {
        'product': product,
        'title': product.nombre + ' | Uomo'
    }

    return render(request, 'shop/product_detail.html', context)
