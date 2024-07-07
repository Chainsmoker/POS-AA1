from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login, get_backends
from django.contrib.auth import get_user_model
from django.contrib import messages

from productos.models import Productos
from ordenes.models import Orden

User = get_user_model()

def login_register(request):
    if request.POST:
        if request.POST.get('action') == 'login':
            email = request.POST.get('login_email')
            password = request.POST.get('login_password')
            if email and password:
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('account:account')
                else:
                    context = {
                        'title': 'Login/Register',
                        'error': 'Correo o contraseña incorrectos. Inténtalo de nuevo.',
                    }
                    return render(request, 'auth/login_register.html', context)   

        elif request.POST.get('action') == 'register':
            name = request.POST.get('register_name')
            last_name = request.POST.get('register_lastname')
            email = request.POST.get('register_email')
            password = request.POST.get('register_password')

            if name and last_name and email and password:
                try:
                    user = User.objects.create_user(username=email, email=email, password=password, nombre=name, apellido=last_name)
                    user = authenticate(request, username=email, password=password)
                    
                    if user is not None:
                        for backend in get_backends():
                            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
                            login(request, user)
                            break
                        return redirect('account:account')

                except Exception as e:
                   print(e)
                   messages.error(request, 'El correo ya está registrado. Inténtalo de nuevo.')
            
            else:
                messages.error(request, 'Todos los campos son requeridos. Inténtalo de nuevo.')
            
            return redirect('/accounts/login/#register-tab')


    context = {
        'title': 'Login/Register | Uomo',
        'active': True
    }
    return render(request, 'auth/login_register.html', context)

def logout_view(request):
    logout(request)
    return redirect('account:login_register')

@login_required
def account(request):
    context = {
        'title': 'My account | Uomo',
        'active': 'dashboard'
    }
    return render(request, 'account/account_dashboard.html', context)

@login_required
def account_address(request):
    context = {
        'title': 'Address | My account',
        'active': 'address'
    }
    return render(request, 'account/account_edit_address.html', context)

@login_required
def account_edit(request):
    if request.POST:
        if request.POST.get('action') == 'edit':
            name = request.POST.get('edit_name')
            last_name = request.POST.get('edit_lastname')
            email = request.POST.get('edit_email')
            if name and last_name and email:
                try:
                    user = request.user
                    user.nombre = name
                    user.apellido = last_name
                    user.email = email
                    user.save()
                    messages.success(request, 'Perfil actualizado correctamente.')
                except Exception as e:
                    print(e)
                    messages.error(request, 'Error al actualizar el perfil.')
            else:
                messages.error(request, 'Todos los campos son requeridos. Inténtalo de nuevo.')
        
        elif request.POST.get('action') == 'change_password':
            password = request.POST.get('edit_password')
            new_password = request.POST.get('edit_new_password')
            confirm_password = request.POST.get('edit_confirm_password')
            if password and new_password and confirm_password:
                if new_password == confirm_password:
                    user = authenticate(request, username=request.user.email, password=password)
                    if user is not None:
                        try:
                            user = request.user
                            user.set_password(new_password)
                            user.save()
                            messages.success(request, 'Contraseña actualizada correctamente. Por favor, inicia sesión nuevamente.')
                            logout(request)
                        except Exception as e:
                            print(e)
                            messages.error(request, 'Error al actualizar la contraseña.')
                    else:
                        messages.error(request, 'La contraseña actual no es correcta. Inténtalo de nuevo.')
                else:
                    messages.error(request, 'Las contraseñas no coinciden. Inténtalo de nuevo.')
            else:
                messages.error(request, 'Todos los campos son requeridos. Inténtalo de nuevo.')
        
        return redirect('account:account_edit')
        
    context = {
        'title': 'Edit | My account',
        'active': 'edit'
    }
    return render(request, 'account/account_edit.html', context)

@login_required
def account_orders(request):
    ordenes = Orden.objects.filter(consumidor=request.user)
    context = {
        'title': 'Orders | My account',
        'active': 'orders',
        'ordenes': ordenes
    }
    return render(request, 'account/account_orders.html', context)

@login_required
def account_wishlist(request):
    context = {
        'title': 'Wishlist | My account',
        'active': 'wishlist'
    }
    return render(request, 'account/account_wishlist.html', context)

@login_required
def account_wishlist_add(request):
    if request.POST:
        user = request.user
        product_id = request.POST.get('product_id')
        if product_id:
            try:
                user = request.user
                product = Productos.objects.get(id=product_id)
                if product in user.wishlist.all():
                    messages.error(request, 'El producto ya está en la lista de deseos.')
                else:    
                    user.wishlist.add(product_id)
                    messages.success(request, 'Producto añadido a la lista de deseos.')
            except Exception as e:
                print(e)
                messages.error(request, 'Error al añadir el producto a la lista de deseos.')
        else:
            messages.error(request, 'Error al añadir el producto a la lista de deseos.')
        
    
    return redirect('account:account_wishlist')

@login_required
def account_wishlist_remove(request):
    if request.POST:
        user = request.user
        product_id = request.POST.get('product_id')
        if product_id:
            try:
                user = request.user
                product = Productos.objects.get(id=product_id)
                if product in user.wishlist.all():
                    user.wishlist.remove(product_id)
                    if user.wishlist.all():
                        messages.success(request, 'Producto eliminado de la lista de deseos.')
                else:
                    messages.error(request, 'El producto no está en la lista de deseos.')
            except Exception as e:
                print(e)
                messages.error(request, 'Error al eliminar el producto de la lista de deseos.')
        else:
            messages.error(request, 'Error al eliminar el producto de la lista de deseos.')
        
    
    return redirect('account:account_wishlist')

