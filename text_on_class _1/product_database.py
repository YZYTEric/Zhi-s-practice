class ProductDatabase:
    def __init__(self):
        self.products = {}  # Format: {product_id: {name, price, quantity}}

    def add_product(self, product_id, name, price, quantity):
        self.products[product_id] = {'name': name, 'price': price, 'quantity': quantity}

    def update_product(self, product_id, name=None, price=None, quantity=None):
        if product_id in self.products:
            if name:
                self.products[product_id]['name'] = name
            if price:
                self.products[product_id]['price'] = price
            if quantity is not None:
                self.products[product_id]['quantity'] = quantity

    def get_product_info(self, product_id):
        return self.products.get(product_id, None)

    def update_stock(self, product_id, quantity):
        if product_id in self.products and self.products[product_id]['quantity'] >= quantity:
            self.products[product_id]['quantity'] -= quantity
            return True
        return False

