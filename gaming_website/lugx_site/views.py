from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.filter(is_featured=True).all()
    return render(request, 'index.html', {"products": products})
def contact(request):
    return render(request, 'contact.html', {})
def shop(request):
    return render(request, 'shop.html', {})
def product(request):
    return render(request, 'product-details.html', {})
