class Car:

    def __init__(self, gas_level):
        self.gas_level = gas_level

    def add_gas(self, added_gas):
        self.gas_level = self.gas_level + added_gas
        return self.gas_level

    def fill_up(self):
        if self.gas_level >= 13.0:
            return 0
        return 13.0 - self.gas_level 

    def __repr__(self):
        return "Gas level = " + str(self.gas_level) + "      (Don't fear the reaper!)"
        #repr only shows when entire class is instantiated. Not just a method...
