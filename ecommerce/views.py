from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from productos.models import Productos
from ordenes.models import Orden, OrdenProducto
from consumidores.models import Consumidores

import json, stripe
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

stripe.api_key = 'sk_test_51PO69TH4Ppt0zy152ViqB4prrYFJoxicD5L3mUrNQt3azPG1Q5KsriYuNVG4x2lAjE5T5FOxvK9eTTa2VVfgjVv100xJkMXNuk'

def remove_duplicates(data):
    unique_ids = set()
    unique_products = []
    
    for product in data:
        product_id = product['productId']
        
        if product_id not in unique_ids:
            unique_products.append(product)
            unique_ids.add(product_id)
    
    return unique_products

def home(request):
    all_products = Productos.objects.all()
    new_products = Productos.objects.order_by('-id')[:5]
    best_sellers = Productos.objects.filter(mas_vendido=True)
    top_rated = Productos.objects.filter(mejor_valorado=True)

    context = {
        'all_products': all_products,
        'new_products': new_products,
        'best_sellers': best_sellers,
        'top_rated': top_rated,
        'title': 'Home | Uomo'
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'title': 'About | Uomo'
    }

    return render(request, 'about.html', context)

def terms(request):
    context = {
        'title': 'Terms | Uomo'
    }

    return render(request, 'terms.html', context)

def store_location(request):
    context = {
        'title': 'Store Location | Uomo'
    }
    return render(request, 'store_location.html', context)

def contact(request):
    context = {
        'title': 'Contact | Uomo'
    }
    return render(request, 'contact.html', context)

def blog(request):
    context = {
        'title': 'Blog | Uomo'
    }
    return render(request, 'blog.html', context)

def shop_cart(request):
    context = {
        'title': 'Cart | Uomo'
    }
    return render(request, 'shop/shop_cart.html', context)

def create_checkout_session(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                data = json.loads(request.body)
                product_quantities = data.get('productIds', [])
                unique_product_quantities = remove_duplicates(product_quantities)
                
                line_items = []

                orden = Orden.objects.create(
                    consumidor=request.user,
                )

                for product_quantity in unique_product_quantities:
                    product_id = product_quantity['productId']
                    quantity = product_quantity['quantity']
                    
                    product = Productos.objects.get(id=product_id)
                    price = int(product.precio * 100)
                    
                    line_items.append({
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': product.nombre,
                                'description': product.mini_descripcion, 
                                #'images': [product.imagenes.first().imagen.url],
                            },
                            'unit_amount': price,
                        },
                        'quantity': quantity,
                    })

                    orden_producto = OrdenProducto.objects.create(
                        producto=product,
                        cantidad=quantity,
                    )
                    orden_producto.save()
                    orden.orden_producto.add(orden_producto)
                
                orden.save()

                session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=line_items,
                    mode='payment',
                    metadata={
                        'order_id': orden.id,
                    },
                    success_url=f'http://127.0.0.1:8000/checkout-complete?session_id={orden.id}',
                    cancel_url='http://127.0.0.1:8000/cart',
                )
                
                return JsonResponse({'checkoutUrl': session.url})
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Datos JSON inválidos'}, status=400)
        else:
            messages.error(request, 'Debes iniciar sesión para realizar una compra.')
            return JsonResponse({'checkoutUrl': '/accounts/login/?next=/cart'})
            
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except stripe.error.SignatureVerificationError as e:
        return JsonResponse({'error': str(e)}, status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order_id = session['metadata']['order_id']
        try:
            order = Orden.objects.get(id=order_id)
            order.pagado = True
            order.estado = 'en camino'
            order.save()
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=400) 

    return JsonResponse({'status': 'success'}, status=200)

def success(request):
    if request.GET.get('session_id'):
        session_id = request.GET.get('session_id')
        try:
            orden = Orden.objects.get(id=session_id)
            if orden.consumidor != request.user:
                return redirect('home')
        except Orden.DoesNotExist:
            return redirect('home')
        
        context = {
            'orden': orden,
        }
        return render(request, 'order_complete.html', context)
    else:
        return redirect('home')