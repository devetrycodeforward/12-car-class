class Car:
    def __init__(self, init_gas_level):
        self.gas_level = init_gas_level
        
    def add_gas(self, gas_added):
        self.gas_level += gas_added
        
    def fill_up(self):
        if self.gas_level < 13:
            amount_of_gas_needed = (13 - self.gas_level)
            self.add_gas(amount_of_gas_needed)
            return amount_of_gas_needed
        return 0
