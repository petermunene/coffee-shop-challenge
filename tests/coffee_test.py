import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee("")          # too short
    with pytest.raises(TypeError):
        Coffee("ab")        # too short
    with pytest.raises(TypeError):
        Coffee(123)         # not a string
    c = Coffee("Latte")
    assert c.name == "Latte"

def test_coffee_name_immutable():
    c = Coffee("Mocha")
    with pytest.raises(AttributeError):
        c.name = "Espresso"

def test_coffee_orders_and_customers():
    Order.all_orders.clear()
    coffee = Coffee("Cappuccino")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    o1 = customer1.create_order(coffee, 4.0)
    o2 = customer2.create_order(coffee, 5.0)

    orders = coffee.orders()
    assert o1 in orders and o2 in orders

    customers = coffee.customers()
    assert customer1 in customers and customer2 in customers
    assert len(customers) == 2

def test_coffee_num_orders_and_average_price():
    Order.all_orders.clear()
    coffee = Coffee("Flat White")
    customer = Customer("Carol")
    assert coffee.num_orders() == 0
    assert coffee.average_price() == 0

    customer.create_order(coffee, 3.0)
    customer.create_order(coffee, 7.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0


