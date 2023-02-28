total1 = int(input("Please enter the first amount raised."))
total2 = int(input("Please enter the second amount raised."))
total3 = int(input("Please enter the third amount raised."))

total = total1 + total2 + total3

print("A total of", "£" + str(total), "was raised.")

if total >= 1000:
    total = total * 2
    print("This will be doubled to", "£" + str(total) + ".")