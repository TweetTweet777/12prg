import math
print("Please enter your three costs.")
num1 = float(input())
num2 = float(input())
num3 = float(input())
total = num1 + num2 + num3
fee = int(round((0.1*total),0))
print("The total cost is £" + str(total))
print("The auction companies fee is £" + str(fee))