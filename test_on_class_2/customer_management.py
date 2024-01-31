# customer_management.py

from product_database import ProductDatabase

class CustomerManagement:
    def __init__(self, product_db):
        self.product_db = product_db

    def record_feedback(self, product_id, rating):
        product = self.product_db.get_product(product_id)
        if product:
            product['feedback'].append(rating)
            # Update the average feedback rating
            total_feedback = sum(product['feedback'])
            count_feedback = len(product['feedback'])
            product['average_feedback'] = total_feedback / count_feedback if count_feedback > 0 else 0.0
        else:
            print("Product not found.")

    def average_rating(self, product_id):
        product = self.product_db.get_product(product_id)
        if product and product['feedback']:
            return sum(product['feedback']) / len(product['feedback'])
        else:
            return "No feedback available."

