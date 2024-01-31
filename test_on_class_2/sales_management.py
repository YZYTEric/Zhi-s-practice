# sales_management.py

from product_database import ProductDatabase

class SalesManagement:
    def __init__(self, product_db):
        self.product_db = product_db

    def record_sale(self, product_id, quantity):
        product = self.product_db.get_product(product_id)
        if product:
            product['sales_history'].append(quantity)
        else:
            print("Product not found.")

    def calculate_total_sales(self, product_id):
        product = self.product_db.get_product(product_id)
        if product:
            return sum(product['sales_history'])
        else:
            return 0

    def best_selling_product(self):
        max_sales = 0
        best_seller = None
        for id, product in self.product_db.products.items():
            total_sales = sum(product['sales_history'])
            if total_sales > max_sales:
                max_sales = total_sales
                best_seller = product['name']
        return best_seller

