import math
def calculate_discount(price, discount_percent):
     result=price*(discount_percent/100)
     return result


def check_calculate_discount(price, discount_percent):
     result=calculate_discount(price, discount_percent)
     if discount_percent>=20:
         return result
     else:
          return price
print(check_calculate_discount(12000,25))     
          