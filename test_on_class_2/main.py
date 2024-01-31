# main.py

from product_database import ProductDatabase
from sales_management import SalesManagement
from customer_management import CustomerManagement
from reporting_system import ReportingSystem

def add_product_ui(product_db):
    print("\n--- Add Product ---")
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    product_db.add_product(product_id, name, price)
    print("Product added successfully!")
   

def record_sale_ui(sales_mgmt):
    print("\n--- Record Sale ---")
    product_id = input("Enter product ID: ")
    quantity = int(input("Enter quantity sold: "))
    sales_mgmt.record_sale(product_id, quantity)
    print("Sale recorded successfully!")
    

def record_feedback_ui(customer_mgmt):
    print("\n--- Record Feedback ---")
    product_id = input("Enter product ID: ")
    rating = float(input("Enter rating (1-5): "))
    customer_mgmt.record_feedback(product_id, rating)
    print("Feedback recorded successfully!")
   

def view_reports_ui(reporting_sys):
    print("\n--- View Reports ---")
    print(f"Total Sales Revenue: ${reporting_sys.total_sales_revenue()}")
    reporting_sys.display_best_selling_product()
    reporting_sys.display_sales_history()
    

def view_average_feedback_ui(customer_mgmt):
    print("\n--- View Product Average Feedback ---")
    product_id = input("Enter product ID: ")
    average_feedback = customer_mgmt.average_rating(product_id)
    if isinstance(average_feedback, float):
        print(f"Average Feedback for Product ID {product_id}: {average_feedback:.2f}")
    else:
        print(average_feedback)

def main_menu():
    print("\n=== Product Sales Analysis System ===")
    print("1. Add Product")
    print("2. Record Sale")
    print("3. Record Feedback")
    print("4. View Reports")
    print("5. View Average Feedback")
    print("6. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    product_db = ProductDatabase()
    sales_mgmt = SalesManagement(product_db)
    customer_mgmt = CustomerManagement(product_db)
    reporting_sys = ReportingSystem(product_db, sales_mgmt, customer_mgmt)

    while True:
        choice = main_menu()
        if choice == '1':
            add_product_ui(product_db)
        elif choice == '2':
            record_sale_ui(sales_mgmt)
        elif choice == '3':
            record_feedback_ui(customer_mgmt)
        elif choice == '4':
            view_reports_ui(reporting_sys)
        elif choice == '5':
            view_average_feedback_ui(customer_mgmt)
        elif choice == "6":
            print("Exiting system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
