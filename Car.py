# Car class
    # constructor function

    #fill_up function

    #add_gas function
class Car:

    def __init__(self,gas_level):
        self.gas_level = float(gas_level)

    def add_gas(self, gas_added):
        self.gas_level = self.gas_level + float(gas_added)

    def fill_up(self):
        if self.gas_level < 13:
            gas_to_be_added = 13 - self.gas_level
            self.add_gas(gas_to_be_added)
            return gas_to_be_added
        if self.gas_level >= 13:
            return 0
