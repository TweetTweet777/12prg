
for loop in range(4):
    print("Week", loop + 1)
    print("Please enter the seven tempuratures.")
    total = 0
    for rep in range(7):
        temp = int(input())
        while (temp > 55) or (temp < -40):
            print("Tempurature should be between -40 and 55")
            temp = int(input())
        total = total + temp

    print("Week", loop + 1, "average was:")
    avg = total /7 
    print(round(avg,2), "degrees centigrade")