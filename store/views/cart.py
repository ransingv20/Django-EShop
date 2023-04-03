from django.shortcuts import render, redirect
from store.models import *
from django.contrib.auth.hashers import  check_password
from django.views import View
from store.models import Product


class Cart(View):
    def get(self, request):
        cart = list(request.session.get("cart").keys())
        products = Product.get_products_by_id_by_list(cart)
        print(products)
        return render(request, 'cart.html',{'cart_products':products})

       