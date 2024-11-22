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
        self.cart[product_id] = quantity
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)

    def get_quants(self):
        return self.cart

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        self.cart[product_id] = product_qty
        self.session.modified = True
        return self.cart

    def delete(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True
    
    def cart_total(self):
        product_ids= self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantites= self.cart
        total =0
        for key, value in quantites.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.sales_price > 0:
                        total= total+(product.sales_price * value)
                    else:
                        total= total+(product.price * value)
        return  total
