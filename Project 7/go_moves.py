    # By submitting this assignment, I agree to the following:
    # "Aggies do not lie, cheat, or steal, or tolerate those who do."
    # "I have not given or received any unauthorized aid on this assignment."
    #
    # Names: James Willard
    # NAME Simon Soto
    # NAME Aidan Patel
    # NAME Kai Fuentes-Hamilton
    # Section: 519
    # Assignment: Lab 7 Activity 1 Team
    # Date: 10 OCT 2025

grid =[['.' for x in range(9)] for z in range(9)] #Creates 9x9 grid filled with '.'

for i in range(9):
    print(' '.join(grid[i])) #Prints initial empty grid (removing commas etc)

black_stone = chr(9675) #Black stone color
white_stone = chr(9679) #White stone color

players = [(black_stone, "Black"), (white_stone, "White")] #Used a tuple to store each stone value to a user's key

stop_game = input("Continue: ").lower() #any form of stop will end the game
while stop_game != "stop": #loops until user types "stop"
    for player in players: #Alternates between players
        stone = player[0] #Assigns stone value
        color = player[1] #Assigns color value
        print(f"{color}'s turn") #Indicates whose turn it is
        row = int(input("Enter row (1-9): ")) - 1 #Subtracts 1 to match list index
        col = int(input("Enter column (1-9): ")) - 1 #Subtracts 1 to match list index
        if grid[row][col] == '.': #Checks if space is empty to place stone
            grid[row][col] = stone
        else:
            while grid[row][col] != '.': #Loops until user selects an empty space and prints error if space isnt empty
                print("Invalid move, try again.")
                print(f"{color}'s turn")
                row = int(input("Enter row (1-9): ")) - 1
                col = int(input("Enter column (1-9): ")) - 1
            if grid[row][col] == '.':
                grid[row][col] = stone
        for i in range(9):
            print(' '.join(grid[i]))
        stop_game = input("Type 'stop' to end the game or press Enter to continue: ").lower() #Asks user if they want to stop the game
        if stop_game == "stop": #stops loop if user types stop
            break