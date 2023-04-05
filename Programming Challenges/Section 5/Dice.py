import random
list = []
count = 0
while not len(list) == 6:
    count = count + 1
    rolled = random.randint(1,6)
    print("Dice Rolled =", rolled)
    if list.count(rolled) >= 1:
        list.remove(rolled)
    else:
        list.append(rolled)
    print("After roll", str(count) +":", list)
print("Game Completed in", count, "rolls of the dice")
