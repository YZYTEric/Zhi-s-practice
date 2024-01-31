

from customer_database import CustomerDatabase
from product_database import ProductDatabase

def process_order(customer_db, product_db, customer_id, product_id, quantity):
    product = product_db.get_product_info(product_id)
    if product and product['quantity'] >= quantity:
        product_db.update_stock(product_id, quantity)
        total_cost = product['price'] * quantity
        order = {'product_id': product_id, 'quantity': quantity, 'total_cost': total_cost}
        customer_db.add_order_to_history(customer_id, order)
        print(f"Order processed. Total cost: ${total_cost}")
    else:
        print("Order cannot be processed due to insufficient stock or invalid product.")

def generate_reports(customer_db, product_db):
    total_sales = 0
    product_sales = {}
    for customer in customer_db.customers.values():
        for order in customer['order_history']:
            total_sales += order['total_cost']
            product_sales[order['product_id']] = product_sales.get(order['product_id'], 0) + order['quantity']
    most_popular_product = max(product_sales, key=product_sales.get, default="None")
    print(f"Total Sales: ${total_sales}")
    print(f"Most Popular Product: {most_popular_product} (Quantity Sold: {product_sales.get(most_popular_product, 0)})")

def main():
    customer_db = CustomerDatabase()
    product_db = ProductDatabase()

    while True:
        print("\nInventory Management System")
        print("1. Process Order")
        print("2. Generate Reports")
        print("3. enter Customer database")
        print("4. enter Product database")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            customer_id = int(input("Enter Customer ID: "))
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter Quantity: "))
            process_order(customer_db, product_db, customer_id, product_id, quantity)
        elif choice == '2':
            generate_reports(customer_db, product_db)
        elif choice == '3':
            while True:
                print("\nCustomer Database")
                print("1. Add Customer")
                print("2. Update Customer")
                print("3. Remove Customer")
                print("4. Get Customer Info")
                print("5. Add Order to History")
                print("6. Exit to Main Menu")
                choice_customer = input("Enter choice: ")

                if choice_customer == '1':
                    customer_id = input("Enter Customer ID: ")
                    name = input("Enter Customer Name: ")
                    contact_details = input("Enter Contact Details: ")
                    customer_db.add_customer(customer_id, name, contact_details)

                elif choice_customer == '2':
                    customer_id = input("Enter Customer ID to update: ")
                    name = input("Enter new name (or press enter to skip): ")
                    contact_details = input("Enter new contact details (or press enter to skip): ")
                    customer_db.update_customer(customer_id, name or None, contact_details or None)

                elif choice_customer == '3':
                    customer_id = input("Enter Customer ID to remove: ")
                    customer_db.remove_customer(customer_id)

                elif choice_customer == '4':
                    customer_id = input("Enter Customer ID: ")
                    info = customer_db.get_customer_info(customer_id)
                    print(info)

                elif choice_customer == '5':
                    customer_id = input("Enter Customer ID: ")
                    order = input("Enter Order Details: ")
                    customer_db.add_order_to_history(customer_id, order)

                elif choice_customer == '6':
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == '4':
            while True:
                print("\nProduct Database")
                print("1. Add Product")
                print("2. Update Product")
                print("3. Get Product Info")
                print("4. Update Stock")
                print("5. Exit to Main Menu")
                choice_product = input("Enter choice: ")

                if choice_product == '1':
                    product_id = input("Enter Product ID: ")
                    name = input("Enter Product Name: ")
                    price = float(input("Enter Product Price: "))
                    quantity = int(input("Enter Product Quantity: "))
                    product_db.add_product(product_id, name, price, quantity)

                elif choice_product == '2':
                    product_id = input("Enter Product ID to update: ")
                    new_name = input("Enter new product name (or press enter to skip): ")
                    new_price = input("Enter new product price (or press enter to skip): ")
                    new_quantity = input("Enter new product quantity (or press enter to skip): ")
                    product_db.update_product(product_id, new_name or None, new_price or None, new_quantity or None)

                elif choice_product == '3':
                    product_id = input("Enter Product ID: ")
                    info = product_db.get_product_info(product_id)
                    print(info)

                elif choice_product == '4':
                    product_id = input("Enter Product ID: ")
                    quantity = int(input("Enter Quantity to update stock: "))
                    product_db.update_stock(product_id, quantity)

                elif choice_product == '5':
                    break

                else:
                    print("Invalid choice. Please try again.")
                    print("Exiting the system.")
                    break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

