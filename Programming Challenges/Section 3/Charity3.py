total1 = int(input("Please enter the first amount raised."))
total2 = int(input("Please enter the second amount raised."))
total3 = int(input("Please enter the third amount raised."))

total = total1 + total2 + total3

print("A total of", "£" + str(total), "was raised.")

if total < 1000:
    total = total + 100
elif total >= 1000 and total <= 2000:
    total = total * 2
else:
    total = 4000 + (total - 2000)

print("This will be doubled to:")
for loop in range(3):
    print("£" + str(total) + "!!!")