
class Coffee:
    def __init__(self, name):
        self.name=name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if not isinstance(value,str) or not (len(value)>=3):
            raise TypeError ("invalid name")
        else:
            self._name=value


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
        average=total/len(prices)
        if not average:
            return 0
        else:
            return average



