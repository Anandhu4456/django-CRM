from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home' ),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>', views.customers, name='customer'),
    path('createOrder/', views.create_order, name='create_order'),
    path('updateOrder/<str:pk>' , views.update_order, name='update_order'),
    path('deleteOrder/<str:pk>', views.delete_order, name='delete_order')
]