class Car:
    #Car class for representing an automobile.

    def __init__(self, initial_fuel):
        #Create a new car with fuel
        self.fuel = initial_fuel
    
    def add_gas(self, gas_added):
        #Add fuel to the car
        self.fuel += gas_added

    def fill_up(self):
        #Fill up the car's fuel tank
        if self.fuel >= 13.0:
            return 0
        amount = 13.0 - self.fuel
        self.add_gas(amount)
        return amount
