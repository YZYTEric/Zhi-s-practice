# test_system.py

from product_database import ProductDatabase
from sales_management import SalesManagement
from customer_management import CustomerManagement
from reporting_system import ReportingSystem

def test_add_product():
    product_db = ProductDatabase()
    product_db.add_product("P001", "Test Product 1", 10.0)
    assert "P001" in product_db.products
    print("test_add_product passed")

def test_record_sale():
    product_db = ProductDatabase()
    sales_mgmt = SalesManagement(product_db)
    product_db.add_product("P002", "Test Product 2", 20.0)
    sales_mgmt.record_sale("P002", 3)
    assert product_db.products["P002"]['sales_history'] == [3]
    print("test_record_sale passed")

def test_record_feedback():
    product_db = ProductDatabase()
    customer_mgmt = CustomerManagement(product_db)
    product_db.add_product("P003", "Test Product 3", 30.0)
    customer_mgmt.record_feedback("P003", 4)
    assert product_db.products["P003"]['feedback'] == [4]
    print("test_record_feedback passed")

def test_average_feedback():
    product_db = ProductDatabase()
    customer_mgmt = CustomerManagement(product_db)
    product_db.add_product("P004", "Test Product 4", 40.0)
    customer_mgmt.record_feedback("P004", 5)
    customer_mgmt.record_feedback("P004", 3)
    assert product_db.products["P004"]['average_feedback'] == 4.0, "Average feedback calculation error"
    print("test_average_feedback passed")
    
def run_tests():
    test_add_product()
    test_record_sale()
    test_record_feedback()
    test_average_feedback()
    print("All tests passed")

if __name__ == "__main__":
    run_tests()

