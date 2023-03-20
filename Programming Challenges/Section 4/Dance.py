name = [""] * 4
age = [0] * 4
level = [""] *4
for loop in range(4):
    name[loop] = input("Please enter a name:")
    print("Please enter", name[loop] + "'s age:")
    age[loop] = int(input())
    if age[loop] < 12:
        level[loop] = "Junior"
    elif age[loop] >= 18:
        level[loop] = "Senior"
    else:
        level[loop] = "Teen"

print("Names and competition List:")

for loop in range(4):
    print(name[loop], "-", level[loop])