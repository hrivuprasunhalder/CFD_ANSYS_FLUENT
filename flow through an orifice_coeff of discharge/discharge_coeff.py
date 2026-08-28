import math

radius = float(input("Radius of the orifice(m): "))
p_up = float(input("Upstream Pressure(Pa): "))
p_down = float(input("Downstream Pressure(Pa): "))
massflowrate_actual = float(input("Actual Mass Flow Rate(kg/s): ")) 


massflowrate_bernoulli = (math.pi * (radius)**2) * (math.sqrt(2 * 1000 *(p_up - p_down)))
discharge_coeff = massflowrate_actual / massflowrate_bernoulli

print("Discharge Co-efficient: ")
print(discharge_coeff)               
               
