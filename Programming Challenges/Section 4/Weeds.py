weeds = [["0"] * 5 for main in range(5)]
total = 0
for row in range(5):
    for column in range(5):
        print("Please enter the number of weeds counted at", str(row + 1) + "," + str(column + 1) + ":")
        weeds[row][column] = int(input())
        total = total + weeds[row][column]

print("The results are shown below:")
for r in range(5):
    for c in range(5):
        print(weeds[r][c],end=' ')
    print("")
print("The total number of weeds found was -", total)
