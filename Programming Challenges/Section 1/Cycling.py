import math
circ = int(input("What is the circumference of your wheel in milimeters?"))
rev = int(input("How many wheel revolutions have taken place in your journey?"))
mins = int(input("How many minutes did you cycle for?"))

distance = (circ * rev) / 1000000
speed = distance / (mins / 60)

print("You covered", distance, "km.")
print("At an average speed of", speed, "kmh.")