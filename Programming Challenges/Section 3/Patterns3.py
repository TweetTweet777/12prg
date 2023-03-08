print("The following program will display odd numbers.")
first = int(input("Enter the first number in the list"))
last = int(input("Enter the last number in the list")) 
while not (last >= (first + 20)):
    print("Sorry, the number must be at least 5+20")
    print("Please re-enter the number")
    last = int(input())

print("Odd numbers list")
for loop in range(first,last + 1,2):
    print(loop)