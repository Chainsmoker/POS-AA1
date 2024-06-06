"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from ecommerce.views import home, shop_cart, create_checkout_session, about, terms, store_location, contact, blog, stripe_webhook, success

app_name = 'ecommerce'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', shop_cart, name='shop_cart'),
    path('about/', about, name='about'),
    path('terms/', terms, name='terms'),
    path('store-location/', store_location, name='store_location'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('checkout/', create_checkout_session, name='create_checkout_session'),
    path('checkout-complete/', success, name='success'),
    path('webhook/', stripe_webhook, name='stripe_webhook'),
    path('', home, name='home'),
    path('', include('productos.urls')),
    path('', include('consumidores.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
