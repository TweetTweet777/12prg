import math
brick = float(input("Please enter the length of a brink in cm:"))
wall = float(input("Please enter the length of the wall in m:"))
total = int((wall*100 / (brick + 1)))
short = wall*100 - (total * (brick + 1))
print(total, "bricks build one row of wall.")
print("This is", int(short), "cm short of the required wall length.")