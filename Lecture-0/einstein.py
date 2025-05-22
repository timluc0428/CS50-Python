#prompt user for mass as an integer in kg
#output the equivalent number of Joules as an integer

mass = input("input the mass in Kg to be converted: ")
mass = int(mass)

speed_of_lightsq = 300000000**2

energy = mass * speed_of_lightsq

print(f"{energy} + Joules")
