from django.shortcuts import render
from product.models import Products , Category

# Create your views here.
def index(request):
    context = {'product' : Products.objects.all()}
    return render(request , 'home/index.html' , context)

def category(request):
    context = {'category' : Category.objects.all()}
    return render(request , 'home/category.html', context)

