from django.shortcuts import render,get_object_or_404
from .cart import Cart
from core.models import Product
from django.http import JsonResponse 
# Create your views here.
def cart_summary(request):
    cart= Cart(request)
    cart_products= cart.get_prods
    quantites= cart.get_quants
    return render(request, 'cart_summary.html',{"cart_products":cart_products,
                                                "quantites":quantites,
    })


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty'))

            if product_qty <= 0:
                raise ValueError("Quantity must be positive.")

            product = get_object_or_404(Product, id=product_id)
            cart.add(product=product, quantity=product_qty)
            cart_quantity = len(cart)
            return JsonResponse({'qty': cart_quantity})
        except (ValueError, Product.DoesNotExist) as e:
            return JsonResponse({'error': str(e)}, status=400)




def cart_delete(request):
    pass

def cart_update(request):
    pass
