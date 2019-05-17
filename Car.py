class Car:
    def __init__(self, gas_level):
        self.gas_level = gas_level

    def get_gaslevel(self):
        return self.gas_level

    def add_gas(self, x):
        new_gaslevel = x + self.gas_level
        return new_gaslevel
    
    def fill_up(self):
        if self.gas_level < 13:
            new_y = 13- self.gas_level
            return new_y
        else: 
            return 0
