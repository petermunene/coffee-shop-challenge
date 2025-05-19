from customer import Customer
from coffee import Coffee

class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Invalid price: must be float between 1.0 and 10.0")
        if not isinstance(customer, Customer):
            raise TypeError("Invalid customer: must be Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("Invalid coffee: must be Coffee instance")

        self._price = float(price)
        self._customer = customer
        self._coffee = coffee

        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        raise AttributeError("Cannot modify customer")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        raise AttributeError("Cannot modify coffee")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        raise AttributeError("Cannot modify price")