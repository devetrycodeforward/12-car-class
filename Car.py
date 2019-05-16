# TODO: add the Car class
# has gas level attribute
# constructor __init__ that takes float representing initial gas level & sets gas level to value
# add_gas method that takes single float value & adds amount to current value
# fill_up method that sets the car's gas level up to 13.0 by adding needed gas to reach it
    ## will return a float of the amount added to get to 13
    ## if has >= 13.0, return 0
class Car:
    def __init__ (self, gas_level):
        self.gas_level = float(gas_level)
    def add_gas (self, extra_gas):
        return self.gas_level + extra_gas
    def  fill_up (self):
        if self.gas_level > 13.0:
            return 0
        return 13.0 - float(self.gas_level)
