print("Please enter the score for each ball.")

overs = 0
over = [0] * 6
for loop in range(6):
    
    over[loop] = int(input())
    overs = overs + over[loop]
    
print("This over's score was:", overs)
print("With each ball scoring:")
for loop in range(6):
    print(over[loop])