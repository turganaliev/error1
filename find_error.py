from datetime import datetime
from enum import Enum


class Condition(Enum):
    NEW = 1
    GOOD = 0.8
    OKAY = 0.5
    BAD = 0.2


class Bike:
    min_profit = 10

    def __init__(self, cost, make, model, year, condition):
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.__sale_price = None
        self.sold = False


    @property
    def sale_price(self):
        if self.__sale_price is None:
            self.update_sale_price()
        return self.__sale_price

    @sale_price.setter
    def sale_price(self, value):
        if value < 0:
            default_sale_price = self.cost + self.min_profit
            print(f'Cannot set sale price to ${value}. Setting to default: ${default_sale_price}')
            self.__sale_price = default_sale_price
        else:
            self.__sale_price = value

    def update_sale_price(self):
        original_value = self.lookup_msrp_value(self.make, self.model)
        current_year = datetime.now().year
        current_value = original_value * (1 - (current_year - self.year) * 0.015)
        current_value = current_value * self.condition.value
        self.sale_price = current_value  # Calls sale_price.setter
        return self.sale_price


    def sell(self):
        self.sold = True
        return self.profit



    def service(self, cost, new_condition):
        self.cost += cost
        self.condition = new_condition
        self.update_sale_price()
        return self.sale_price


    @property
    def profit(self):
        if not self.sold:
            return None
        return self.sale_price - self.cost


    @staticmethod
    def lookup_msrp_value(make, model):
        return 1000

    @classmethod
    def get_default_bike(cls):
        return cls(
            cost=0,
            make='A make',
            model='A model',
            year=2010,
            condition=Condition.GOOD
                )
#
if __name__ == '__main__':
    bike = Bike.get_default_bike()
    bike.sell()
    print(bike.profit)
