from django.shortcuts import render
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from core.forms import UpdateUserForm
from django.contrib.auth.models import User

def checkout(request):
    cart = Cart(request) 
    cart_products = cart.get_prods() 
    quantities = cart.get_quants()
    totals = cart.cart_total()
    ttotals=0
    if totals > 0:
        ttotals=totals+120
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        # Get the ShippingAddress instance for the logged-in user
        shipping_user = ShippingAddress.objects.filter(user=current_user).first()
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)  
        return render(request, 'payment/checkout.html', {
            "cart_products": cart_products, 
            "quantities": quantities,
            "totals": totals,
            "shipping_form": shipping_form,
            "ttotals" : ttotals,
        })
    else:
        shipping_form = ShippingForm(request.POST or None)
        return render(request, 'payment/checkout.html', {
            "cart_products": cart_products, 
            "quantities": quantities,
            "totals": totals,
            "shipping_form": shipping_form,
        })
        
def payment_success(request):
    return render(request, "payment/payment_success.html",{})


