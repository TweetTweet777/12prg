import math
area = int(input("Enter the area in m2 to be painted."))
pot = int(input("Enter the area (m2) that a single pot covers."))
pots = math.ceil(area/pot)
leftover = (pot*pots) - area

print("You will need", pots, "pots of paint.")
print("You can paint", leftover, "m2 with the leftover paint.")
