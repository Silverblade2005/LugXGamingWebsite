from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def home(request):
    trending = Product.objects.filter(is_featured=True).all()
    most_played = Product.objects.filter().order_by('-total_plays').all()[:6]
    top_categories = Category.objects.filter().order_by('-total_searched').all()[:5]

    return render(request, 'index.html', {
        "trending": trending,
        "most_played": most_played,
        "top_categories": top_categories,
        })

def contact(request):
    return render(request, 'contact.html', {})

def shop(request):
    return render(request, 'shop.html', {})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product-details.html', {'product': product})
