seats = [["empty"] * 4 for main in range(5)]

count = -1
count = int(input("How many members have requested a seat?"))
while (count <=0 or count > 20):
    print("Limited to 20 seats")
    count = int(input())

for loop in range(count):
    name = input("Please enter your name.")
    row = int(input("Which row would you like to sit in?"))
    column = int(input("Which seat number would you like to sit in?"))
    seats[row][column] = name
    print("Thank you, your name has been added.")

print("Bus seats have been booked as follows:")
for r in range(5):
    print(str(r) + ".",end=' ')
    for c in range(4):
        print(seats[r][c],end=' ')
    print("")
    
        