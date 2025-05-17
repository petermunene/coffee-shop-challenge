
class Customer:
    def __init__(self, name):
        self.name=name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if not isinstance(value,str) or not (0<len(value)<16):
            raise TypeError ("Invalid name")
        else:
            self._name=value
    def orders(self):
        from order import Order
        orders=[]
        for order in Order.all_orders:
            if order.customer==self:
                orders.append(order)
        return orders

    def coffees(self):
        from order import Order
        coffees=[]
        for order in Order.all_orders:
            if order.customer==self:
                coffees.append(order.coffee)
        return coffees

    def create_order(self,coffee,price):
        from order import Order
        return Order(self,coffee,price)

    @classmethod
    def most_aficionado(cls,coffee):
        customer_spending={}
        from order import Order
        for order in Order.all_orders:
            if coffee==order.coffee:
                customer=order.customer
                customer_spending[customer]=customer_spending.get(customer,0) + order.price
        if not customer_spending:
            return None
        else:
            return max(customer_spending, key=customer_spending.get)

                    
        
                


        




 