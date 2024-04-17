from django.shortcuts import render
from .models import Product

def home(request):
    product = Product.objects.all()
    return render(request, 'home_app/index.html', {"product_list" : product})
