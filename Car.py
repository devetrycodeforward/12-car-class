class Car:

    def __init__(self, init_gas):
        self.gas = init_gas

   
    def add_gas(self, gas_fill):
        self.gas + gas_fill


    def fill_up(self):
        if self.gas < float(13.00):
            gas_fill = (13.00 - (self.gas))
            self.add_gas(gas_fill)
        else:
            return 0
        return gas_fill
        
def main():
    example_car = Car(12.5)
    print(example_car.fill_up())
    another_car = Car(18)
    print(another_car.fill_up())

if __name__=="__main__":
    main()
