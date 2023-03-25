from django.shortcuts import render, HttpResponse , redirect
from django.http import HttpResponseRedirect
from product.models import Products , Category
from accounts.models import Cart , CartItem


# Create your views here.


def get_product(request , slug):
    try:
        product = Products.objects.get(slug = slug)
        context= {'product': product}
        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_by_size(size)
            context['selected_size']=size
            context['updated_price']=price
            print(price)
        return render(request , 'product/product.html', context = context)
    except Exception as e:
        print(e)


def add_to_cart(request , uid):
    variant = request.GET.get('variant')
    product = Products.objects.get(uid = uid)
    user = request.user
    cart , _ = Cart.objects.get_or_create(user = user , is_paid = False)
    cart_item = CartItem.objects.create(cart = cart , product= product ,)

    if variant:
        variant = request.GET.get('variant')
        size_variant = Sizevariant
    return HttpResponseRedirect(request.path_info)


def get_categories(reuest , category_name ):
    try:
        product = Products.objects.filter(category_name = category).values()
        context = {'product': product}
        return render(request , 'home/index2.html',context=context)
    except Exception as e:
        print(e)

