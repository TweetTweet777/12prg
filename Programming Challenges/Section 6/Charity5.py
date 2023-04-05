def tot(aa):
    total = 0
    for loop in range(aa):
        money = int(input())
        total = total + money
    return total

def calc(total):
    if total < 1000:
        total = total + 100
    elif total >= 1000 and total <= 2000:
        total = total * 2
    else:
        total = 4000 + (total - 2000)
    return total

aa = int(input("How many charity raisers were there?"))
total = 0

print("Enter the total raised by each:")
total = tot(aa)

print("A total of", "£" + str(total), "was raised.")
total = calc(total)


print("This will be increased to:")
for loop in range(3):
    print("£" + str(total) + "!!!")