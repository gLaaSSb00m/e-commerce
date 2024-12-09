from django.shortcuts import render,get_object_or_404,redirect
from .cart import Cart
from core.models import Product
from django.http import JsonResponse 
# Create your views here.
def cart_summary(request): 
    cart = Cart(request) 
    cart_products = cart.get_prods() 
    quantities = cart.get_quants()
    totals = cart.cart_total()

    return render(request, 'cart_summary.html', {
        "cart_products": cart_products, 
        "quantities": quantities,
        "totals": totals,
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
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'post':
        try:
            product_id = str(request.POST.get('product_id'))  # Get the product ID from the request
            if product_id in cart.cart:
                del cart.cart[product_id]  # Delete the product from the cart
                cart.session.modified = True  # Mark the session as modified
                return JsonResponse({'message': 'Product removed successfully'})
            else:
                return JsonResponse({'error': 'Product not found in cart'}, status=400)
        except KeyError:
            return JsonResponse({'error': 'Invalid request'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def cart_update(request):
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty'))
            cart.update(product=product_id, quantity=product_qty)
            return JsonResponse({'qty': product_qty})
        except (ValueError, KeyError) as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

