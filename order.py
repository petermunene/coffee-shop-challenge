from .customer import Customer
from .coffee import Coffee

class Order:
    all_orders=[]
    def __init__(self, customer, coffee, price):
        if  isinstance (customer,Customer):
            self._customer=customer
        else:
            raise TypeError("invalid customer")
        if  isinstance (coffee,Coffee):
            self._coffee=coffee
        else:
            raise TypeError("invalid coffee")
        self.price=price
        Order.all_orders.append(self)
    @property
    def customer(self):
        return self._customer
    @property
    def coffee(self):
        return self._coffee
    @property
    def price(self):
        return self._price
    @price.setter
    def price (self,value):
        if isinstance(value,(int,float)) and 1.0 <= value <= 10.0:
            self._price=value
        else:
            raise ValueError("invalid")

