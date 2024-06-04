from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_customers = customers.count()
    total_orders = orders.count()
    
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    context = {'orders':orders, 'customers':customers,
            'total_orders':total_orders,
            'delivered':delivered,'pending':pending}
    
    return render(request, 'accounts/dashboard.html',context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html',{'products':products})


def customers(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()  #get orders of the customer
    order_count = orders.count()
    context = {'customer':customer,'orders':orders,'order_count':order_count}
    return render(request, 'accounts/customers.html',context)


def create_order(request):
    form = OrderForm()
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to home
            return redirect('/')
        
    context = {'form':form}
    return render(request, 'accounts/order_form.html',context)
