from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    torders = orders.count()
    porders = orders.filter(status='Pending').count()
    dorders = orders.filter(status='Delevered').count()
    oorders = orders.filter(status='out of order').count()
    iorders = orders.filter(status='in progress').count()
    context = {
            'customers': customers,
             'orders'  : orders,
             'torders' : torders,
             'dorders' : dorders,
             'iorders' : iorders,
             'oorders' : oorders,
             'porders' : porders,
             }
    return render(request, 'bookstore/dashboard.html',context)

def books(request):
    books = Book.objects.all()
    return render(request, 'bookstore/books.html',{'books': books})

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    torders = orders.count()
    context = {
        'customer':customer,
        'orders':orders,
        'torders':torders,
    }
    return render(request, 'bookstore/customer.html',context)

def profile(request):
    return render(request, 'bookstore/profile.html')