# Car class
class Car:
    def __init__(self, init_gas_level):
        """ Create a new car and set its initial gas level """ 
        self.gas_level = init_gas_level

    def get_gas(self):
        return self.gas_level

    def add_gas(self, gas):
        # takes a single float value and adds this amount to the current value of 
        return gas + self.get_gas()

    def fill_up(self):
        current_level = self.get_gas() 
        difference = 13 - current_level 
        if current_level < 13:
            self.add_gas(difference) 
            return difference
        else:
            return 0
