class Car:
  def __init__(self, init_gas_level):
    self.gas_level = init_gas_level

  def add_gas(self, gas_to_add):
    self.add_gas = float(gas_to_add)
    self.gas_level = (self.gas_level + gas_to_add)
    return self.gas_level
  
  def fill_up(self):
    if self.gas_level <13:
      return (13 - (self.gas_level))
    else:
      return 0


