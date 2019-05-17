class Car:
    def __init__( self, gas_level):
        self.gas_level = float(gas_level)
        
    def add_gas (self, add_gas):
        self.gas_level = (self.gas_level + float(add_gas))
        return self.gas_level

    def fill_up(self):
        if self.gas_level <13:
            return (13 - (self.gas_level))
        else:
            return 0
