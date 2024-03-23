from django.shortcuts import render
from .models import Product, Category, Tags

# Create your views here.
def home(request):
    trending = Product.objects.filter(is_featured=True).all()
    most_played = Product.objects.filter().order_by('-total_plays').all()[:6]
    top_categories = Category.objects.filter().order_by('-total_searched').all()[:5]

    return render(request, 'index.html', {
        "trending": trending,
        "most_played": most_played,
        "top_categories": top_categories,
        "default_page_num": 1,
        })

def contact(request):
    return render(request, 'contact.html', {
        "default_page_num": 1,
    })

def shop(request, pk):
    all_products = Product.objects.all()
    previous_page = pk - 1
    next_page = pk + 1
    content_start = 20 * (pk - 1)
    content_end = content_start + 20
    if len(all_products) + 19 < next_page * 20:
        next_page = 1

    if previous_page == 0:
        previous_page = 1

    return render(request, 'shop.html', {
        "default_page_num": 1,
        'all_products': all_products[content_start:content_end],
        "tags": Tags.objects.all(),
        "products_per_page": 20,
        "current_page": pk,
        'prev_page': previous_page,
        "next_page": next_page,
    })

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product-details.html', {
        'product': product,
        "default_page_num": 1,
    })
