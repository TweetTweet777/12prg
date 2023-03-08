print("Please enter the seven tempuratures.")

total = 0
for loop in range(7):
    temp = int(input())
    total = total + temp

print("This week's average was:")
avg = total /7 
print(round(avg,2), "degrees centigrade")