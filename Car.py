class Car:
    """car class for determing gas levels"""
    def __init__(self, gas_level):
        
        self.gas_level = gas_level
        gas_level = 0
        
    def add_gas(self, amount):
        self.gas_level += float(amount) 
    
    def fill_up(self):
        amount = float
        if self.gas_level >= 13:
            return 0
        else: 
            amount = (13 - self.gas_level)
            self.add_gas(amount)
            return amount
    

