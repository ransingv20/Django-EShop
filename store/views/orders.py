from django.shortcuts import  redirect, render
from store.models import *
from django.views import View
from store.models import Product
from store.middleware.auth import auth_middleware
from django.utils.decorators import method_decorator

class Orders(View):

    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        # print(orders)
        return render(request, 'orders.html', {'products':orders})