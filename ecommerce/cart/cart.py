from core.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if not cart:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = quantity  # Add new product
        self.session.modified = True

    def __len__(self):
        return len(self.cart)  # Total quantity in cart

    def get_prods(self):
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)
    def get_quants(self):
        quantities= self.cart
        return quantities
