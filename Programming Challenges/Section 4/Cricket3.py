another = "y"
while another == "y" or another == "Y":
    overs = [0] * 2
    over = [[0] * 6 for main in range(6)]

    for team in range(2):
        for count in range(3):
            print("Please enter over", count + 1,"for Team", team + 1)
            for column in range(6):
                over[team + count][column] = int(input())
                overs[team] = overs[team] + over[team + count][column]

    print("Score for Team 1's three overs:")
    print(overs[0])
    print("Score for Team 2's three overs:")
    print(overs[1])
    if overs[0] > overs[1]:
        team = 1
    else:
        team = 2
    print("Team", team, "won the match.")
    another = input("Do you wish to calculate the result of another game?")