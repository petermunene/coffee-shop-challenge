import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from order import Order
from customer import Customer
from coffee import Coffee

def test_order_price_validation():
    cust = Customer("TestUser")
    coffee = Coffee("Latte")
    
    with pytest.raises(ValueError, match="Invalid price: must be float between 1.0 and 10.0"):
        Order(cust, coffee, 0.5)
    
    with pytest.raises(ValueError, match="Invalid price: must be float between 1.0 and 10.0"):
        Order(cust, coffee, 15.0)

    with pytest.raises(ValueError, match="Invalid price: must be float between 1.0 and 10.0"):
        Order(cust, coffee, "five")

def test_order_customer_validation():
    coffee = Coffee("Espresso")
    
    with pytest.raises(TypeError, match="Invalid customer"):
        Order("NotACustomer", coffee, 5.0)

def test_order_coffee_validation():
    cust = Customer("Alice")
    
    with pytest.raises(TypeError, match="Invalid coffee"):
        Order(cust, "NotACoffee", 5.0)

def test_order_attributes():
    cust = Customer("Alice")
    coffee = Coffee("Mocha")
    order = Order(cust, coffee, 4.5)

    assert order.customer == cust
    assert order.coffee == coffee
    assert order.price == 4.5
    assert order in Order.all_orders

    