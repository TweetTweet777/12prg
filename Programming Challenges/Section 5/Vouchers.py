seat = [-1] * 56
wish = "Y"

while wish == "Y":
    age = int(input("Enter age:"))
    number = int(input("Enter seat:"))
    seat[(number - 1)] = age
    wish = input("Do you wish to enter another:").upper()

oldest = seat.index(max(seat)) + 1
count = seat.count(0)
print("The oldest audience member is sitting in seat", oldest)
print(count,"audience members did not give their age")