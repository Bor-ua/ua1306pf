FREEZING_POINT = 0
BOILING_POINT = 0
def print_water_state(temperature):
      if temperature <= FREEZING_POINT:
             print("Solid")
      elif FREEZING_POINT < temperature < BOILING_POINT:
             print("Liquid")
      else:
             print("Gas")