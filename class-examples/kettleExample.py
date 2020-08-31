class Kettle(object):

    # power_source = "electricity"

    def __init__(self, make, price):  # self is a refrence to the instance of the class
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


def kettle1(make, price):
    return {'make': make,
            'price': price}


print('-----------')
phillips = kettle1('Phillips', 15.95)
phillips['make'] = 'samsung'
electrolux = kettle1('Electrolux', 17.45)
print(phillips)
print(phillips.get('make'))
print(phillips.get('price'))

print(electrolux.get('make'))
print(electrolux.get('price'))
print('-----------')

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)
print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)
kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("hamilton", 14.55)
print(hamilton.on)
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

"""
class: template for creating objects, all objects created using the same class
object: an instance of a class 
Instantiate: create a instance of a class
Method: a function defined in a class  
Atribute: a variable bound to an instance of a class
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 50)

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)

print("switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("switch kenwood to gas")
kenwood.power_source = 'gas'
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
