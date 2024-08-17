from django.shortcuts import render,redirect
from django.views.generic import View
from main.models import Product
from .models import Cart,CartProducts

def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create() # yangi cart object hosil qilish
        request.session['user_cart_id'] = cart.id
    return cart


# Create your views here.
class CartView(View):
    def get(self, request):
        cart = cart_init(request)
        return render(request, "cart.html",{"cart":cart})

def add_product(request, pk):
    cart = cart_init(request)
    cart.add(pk)
    if CartProducts.objects.filter(id=pk).exists():
        cart.total_quantity += 1
        cart.total_price += Product.objects.get(id=pk).get_discount_price()
        cart.save()
    return redirect("/cart/")

def cart_product_update(request,action,product_id,item_id):
    cart = cart_init(request)
    item = CartProducts.objects.get(id=item_id)
    if action == "minus":
        item.quantity -= 1
        item.save()
        cart.total_quantity -= 1
        cart.total_price -= item.price
        cart.save()
        if cart.total_quantity == 0:
            cart.delete()
            return redirect("/")
        elif item.quantity == 0:
            item.delete()
            item.save()
    else:
        cart.cart_product_update(action,product_id,item_id)
    return redirect("/cart/")


