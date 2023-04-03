from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import *
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
# Create your views here.

class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        all_products = None
        all_categories = Category.get_all_categories()
        category_id = request.GET.get('category')
        if category_id:
            all_products = Product.get_product_by_id(category_id)
        else:
            all_products = Product.get_all_products()
        data = {}
        data['products'] = all_products
        data['categories'] = all_categories
        print(request.session.get("customer_email"))
        return render(request, 'index.html', data)

    def post(self, request):
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:    
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:    
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(cart)    
        return redirect('homepage')

    



