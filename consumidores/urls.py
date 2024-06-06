from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('accounts/login/', views.login_register, name='login_register'),
    path('accounts/logout/', views.logout_view, name='logout_view'),
    path('accounts/my-profile/', views.account, name='account'),
    path('accounts/my-profile/address/', views.account_address, name='account_address'),
    path('accounts/my-profile/edit/', views.account_edit, name='account_edit'),
    path('accounts/my-profile/orders/', views.account_orders, name='account_orders'),
    path('accounts/my-profile/wishlist/', views.account_wishlist, name='account_wishlist'),
    path('accounts/my-profile/wishlist/add/', views.account_wishlist_add, name='account_wishlist_add'),
    path('accounts/my-profile/wishlist/remove/', views.account_wishlist_remove, name='account_wishlist_remove'),
]