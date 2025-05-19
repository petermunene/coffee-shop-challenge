# coffee-shop-challenge
☕ Coffee Order App
A simple Python OOP-based application for modeling a coffee ordering system involving Customer, Coffee, and Order classes. This project includes comprehensive tests using pytest to ensure all functionality is working as intended.

# Features
# Customer
Stores a name (must be a string between 1–15 characters).

Name is immutable after initialization.

Can:

View their Orders

View unique Coffees they’ve ordered

Create new Orders

Class method to determine the most aficionado customer for a coffee (based on total spend).

# Coffee
Stores a name (must be a string with at least 3 characters).

Name is immutable after initialization.

Can:

View all Orders for the coffee

View unique Customers who ordered it

Calculate total number of orders

Calculate average price from all orders

# Order
Requires:

A Customer instance

A Coffee instance

A price (float between 1.0 and 10.0)

All properties are validated and immutable after creation.


# Getting Started
Requirements
Python 3.8.13

# Project Structure

project/
│
├── customer.py       # Customer class
├── coffee.py         # Coffee class
├── order.py          # Order class
├── tests/
│   ├── test_customer.py
│   ├── test_coffee.py
│   └── test_order.py
└── README.md


# Bonus functionality (most_aficionado) is included and fully tested.

# Author
Peter Munene