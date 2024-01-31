# product_database.py

class ProductDatabase:
    def __init__(self):
        self.products = {}  # format: {product_id: {'name': str, 'price': float, 'sales_history': [], 'feedback': []}}

    def add_product(self, product_id, name, price):
        if product_id not in self.products:
            self.products[product_id] = {
                'name': name, 
                'price': price, 
                'sales_history': [], 
                'feedback': [],
                'average_feedback': 0.0  # Ensure this key is initialized for every new product
            }
        else:
            print("Product already exists.")

    def get_product(self, product_id):
        return self.products.get(product_id, None)

    
