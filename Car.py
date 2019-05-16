
class Car:
    # constructor function
    def __init__(self, gas_level):
        self.gas = float(gas_level)

    #fill_up function
    def fill_up(self):
        if self.gas >= 13:
            return 0
        else:
            return 13 - self.gas
