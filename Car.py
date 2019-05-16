class Car:

    def __init__(self, gas_level):
        self.gas_level = float(gas_level) 

    def add_gas(self, gas_needed):
        self.gas_level += float(gas_needed)

    def fill_up(self):
        gas_needed = 13.0 - self.gas_level
        if gas_needed > 0:
            self.add_gas(gas_needed)
            return float(gas_needed)
        else:
            return 0

