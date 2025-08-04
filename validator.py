import re

def cashier_validator(cashier):
    errors = []
    if not (type(cashier.id) == int and cashier.id>0):
        errors.append('cashier ID must be an integer > 0')

    if not (type(cashier.product_name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", cashier.product_name)):
        errors.append('product Name is Invalid')

    if not (type(cashier.username) == str and re.match(r"^[a-zA-Z\s]{3,30}$", cashier.username)):
        errors.append('cashier family is Invalid')

    if not (type(password) == str and re.match(r"^[a-zA-Z\s]{3,30}$", cashier.password)):
        errors.append(' password must be an integer > 0')


    return errors


