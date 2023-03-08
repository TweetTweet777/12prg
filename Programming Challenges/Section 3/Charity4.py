aa = int(input("How many charity raisers were there?"))

print("Enter the total raised by each:")
total = 0
for loop in range(aa):
    money = int(input())
    total = total + money

print("A total of", "£" + str(total), "was raised.")

if total < 1000:
    total = total + 100
elif total >= 1000 and total <= 2000:
    total = total * 2
else:
    total = 4000 + (total - 2000)

print("This will be increased to:")
for loop in range(3):
    print("£" + str(total) + "!!!")