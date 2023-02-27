import math
circ = input("What is the circumference of your wheel in milimeters?")
rev = input("How many wheel revolutions have taken place in your journey?")
mins = input("How many minutes did you cycle for?")

distance = (circ * rev) / 1000000
speed = distance/(mins/60)

print("You covered", distance, "km.")
print("At an average speed of")