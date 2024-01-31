class CustomerDatabase:
    def __init__(self):
        self.customers = {}  # Format: {customer_id: {name, contact_details, order_history}}

    def add_customer(self, customer_id, name, contact_details):
        self.customers[customer_id] = {'name': name, 'contact_details': contact_details, 'order_history': []}

    def update_customer(self, customer_id, name=None, contact_details=None):
        if customer_id in self.customers:
            if name:
                self.customers[customer_id]['name'] = name
            if contact_details:
                self.customers[customer_id]['contact_details'] = contact_details

    def remove_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]

    def get_customer_info(self, customer_id):
        return self.customers.get(customer_id, None)

    def add_order_to_history(self, customer_id, order):
        if customer_id in self.customers:
            self.customers[customer_id]['order_history'].append(order)
