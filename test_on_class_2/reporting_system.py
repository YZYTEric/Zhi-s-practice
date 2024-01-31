# reporting_system.py

from product_database import ProductDatabase
from sales_management import SalesManagement
from customer_management import CustomerManagement

class ReportingSystem:
    def __init__(self, product_db, sales_mgmt, customer_mgmt):
        self.product_db = product_db
        self.sales_mgmt = sales_mgmt
        self.customer_mgmt = customer_mgmt

    def total_sales_revenue(self):
        total_revenue = 0
        for product in self.product_db.products.values():
            total_sales = sum(product['sales_history'])
            revenue = total_sales * product['price']
            total_revenue += revenue
        return total_revenue

    def display_best_selling_product(self):
        best_seller = self.sales_mgmt.best_selling_product()
        print(f"Best Selling Product: {best_seller}")

    def display_sales_history(self):
        for id, product in self.product_db.products.items():
            print(f"ID: {id}, Name: {product['name']}, Total Sales: {sum(product['sales_history'])}")

