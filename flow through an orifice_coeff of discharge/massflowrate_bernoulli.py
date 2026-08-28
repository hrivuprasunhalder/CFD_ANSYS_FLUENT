import math

p_up = float(input("Upstream Pressure(Pa): "))
p_down = float(input("Downstream Pressure(Pa): "))
radius = float(input("Radius of the orifice(m): "))

massflowrate_bernoulli = (math.pi * (radius)**2) * (math.sqrt(2 * 1000 *(p_up - p_down)))

print("Theoritical Mass Flow Rate")
print(massflowrate_bernoulli)               
               
