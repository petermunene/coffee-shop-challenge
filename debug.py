from customer import Customer
from coffee import Coffee
from order import Order

# Debugging setup
print("=== Coffee Shop Debug Console ===\n")

# Create some customers
alice = Customer("Alice")
bob = Customer("Bob")
print(f"Created customers: {alice.name}, {bob.name}")

# Create some coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")
print(f"Created coffees: {latte.name}, {espresso.name}")

# Create orders
order1 = alice.create_order(latte, 5.0)
order2 = alice.create_order(espresso, 4.5)
order3 = bob.create_order(latte, 6.0)

print("\n--- Orders ---")
for order in alice.orders():
    print(f"{alice.name} ordered {order.coffee.name} for ${order.price}")

for order in bob.orders():
    print(f"{bob.name} ordered {order.coffee.name} for ${order.price}")

# Unique coffees per customer
print("\n--- Unique Coffees ---")
print(f"{alice.name}'s Coffees: {[coffee.name for coffee in alice.coffees()]}")
print(f"{bob.name}'s Coffees: {[coffee.name for coffee in bob.coffees()]}")

# Coffee aggregates
print("\n--- Coffee Order Stats ---")
print(f"{latte.name} total orders: {latte.num_orders()}")
print(f"{latte.name} average price: ${latte.average_price():.2f}")

# Most aficionado
top_customer = Customer.most_aficionado(latte)
print(f"\nTop spender on {latte.name}: {top_customer.name if top_customer else 'None'}")

# Invalid scenarios
print("\n--- Invalid Examples ---")
try:
    bad_customer = Customer("")
except Exception as e:
    print(f"Invalid customer: {e}")

try:
    bad_coffee = Coffee("AB")
except Exception as e:
    print(f"Invalid coffee: {e}")

try:
    bad_order = Order(alice, latte, 100.0)
except Exception as e:
    print(f"Invalid order: {e}")