stock = []
display = False
while display == False:
    status = input("Do you wish to add (A) or remove (R) a dress?").upper()
    size = int(input("Please enter a new dress size:"))
    if size == 999:
        display = True
    elif status == "A":
        stock.append(size)
    elif status == "R":
        stock.remove(size)
    print("Stock =", stock)
print("The largest dress in stock is size", max(stock))
print("The smallest dress in stock is size", min(stock))