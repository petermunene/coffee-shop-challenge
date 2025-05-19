
class Coffee:
    def __init__(self, name):
        if not isinstance(name,str) or not (len(name)>=3):
            raise TypeError ("Invalid name")
        self._name=name
    @property
    def name(self):
        return self._name
    def orders(self):
        from order import Order
        orders=[]
        for order in Order.all_orders:
            if order.coffee==self:
                orders.append(order)
        return orders


    def customers(self):
        from order import Order
        customers=[]
        for order in Order.all_orders:
            if order.coffee==self:
                customers.append(order.customer)
        return customers

    def num_orders(self):
        from order import Order
        num_orders=[]
        for order in Order.all_orders:
            if order.coffee==self:
                num_orders.append(order)
        if len(num_orders)==0:
            return 0
        else :
            return len(num_orders)
    def average_price(self):
        prices=[]
        from order import Order
        for order in Order.all_orders:
            if order.coffee==self:
                prices.append(order.price)
        total=sum(prices)
        
        if not len(prices):
            return 0
        else:
            return total/len(prices)



