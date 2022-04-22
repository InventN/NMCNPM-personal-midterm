from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'acc/dashboard.html')

def products(request):
    return render(request, 'acc/products.html')

def customer(request):
    return render(request, 'acc/customer.html')   

# Create your views here.
