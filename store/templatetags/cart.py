from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False  

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='price_total')
def price_total(product, cart):
    return product.price * cart_quantity(product, cart)



@register.filter(name='sum_of_cart_product')
def sum_of_cart_product(product, cart):
    total = 0
    for p in product:
        total += price_total(p, cart)
    return total