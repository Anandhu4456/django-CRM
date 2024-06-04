from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home' ),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>', views.customers, name='customer'),
    path('createOrder/', views.create_order, name='create_order')
]