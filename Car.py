class Car:
    def __init__(self, gas_level):
        self.x = gas_level
        
    def add_gas(self):
        return self.x + 30
    
    def fill_up(self):
        if self.x >= 13:
            return 0
        else:
            return 13 - self.x
        
