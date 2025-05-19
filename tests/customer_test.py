import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer("")          # empty string not allowed
    with pytest.raises(TypeError):
        Customer("a" * 16)    # longer than 15 chars not allowed
    with pytest.raises(TypeError):
        Customer(123)         # not a string
    # valid name
    cust = Customer("Alice")
    assert cust.name == "Alice"

def test_customer_name_setter():
    cust = Customer("Alice")
    with pytest.raises(AttributeError):
        cust.name = "Bob"

def test_customer_orders_and_coffees():
    cust = Customer("Alice")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Mocha")
    
    order1 = Order(cust, coffee1, 3.5)
    order2 = Order(cust, coffee2, 4.0)
    order3 = Order(cust, coffee1, 5.0)
    
    orders = cust.orders()
    coffees = cust.coffees()
    
    assert len(orders) == 3
    assert set(coffees) == {coffee1, coffee2}

def test_create_order():
    cust = Customer("Bob")
    coffee = Coffee("Espresso")
    order = cust.create_order(coffee, 5.5)
    
    assert order in cust.orders()
    assert order.coffee == coffee
    assert order.price == 5.5
    assert order.customer == cust

def test_most_aficionado():
    cust1 = Customer("Alice")
    cust2 = Customer("Bob")
    coffee = Coffee("Flat White")
    
    Order.all_orders.clear()
    Order(cust1, coffee, 5.0)
    Order(cust1, coffee, 3.0)
    Order(cust2, coffee, 10.0)
    
    # Bob spent 10, Alice spent 8
    assert Customer.most_aficionado(coffee) == cust2
    
    # No orders for coffee2
    coffee2 = Coffee("Americano")
    assert Customer.most_aficionado(coffee2) is None