from itertools import product

from validator import cashier_validator
from model.validator import *

class casheir:
    def __init__(self,id, product_name,username,password):
        self.id = id
        self.productname = product_name
        self.username = username
        self.password = password

    def save (self):
        print(f"{self.id}-{self.productname}-{self.username}-{self.password}saved")

    def to_tuple(self):
        return (self.id, self.productname, self.username, self.password)

    def validator(self):
        return cashier_validator(self)
