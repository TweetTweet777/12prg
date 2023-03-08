print("Please enter the score for each ball.")

overs = 0
for loop in range(6):
    
    over = int(input())
    overs = overs + over
    
print("This over's score was:", overs)