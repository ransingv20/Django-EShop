from django.shortcuts import  redirect
from store.models import *
from django.views import View
from store.models import Product


class Checkout(View):
    def post(self, request):
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        customer = request.session.get("customer")
        cart = request.session.get('cart')
        all_products = Product.get_products_by_id_by_list(list(cart.keys()))

        for product in all_products:
            order = Order(customer=Customer(id=customer), products=product, price=product.price, quantity=cart.get(str(product.id)), phone=phone, address=address)
            order.place_order()
        request.session['cart'] = {}
        return redirect('cart')
       