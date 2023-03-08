password = "ornery"
guess = ""
while not guess == "ornery":
    guess = input("Please enter the password")
    if not guess == "ornery":
        print("Sorry, incorrect! Try again.")
print("Entry Gained!")