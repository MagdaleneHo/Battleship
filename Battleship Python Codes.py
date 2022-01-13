from random import randint

board = [] #stored in a list
board_size = 60  #column is 60
board_top = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# creating the board
def print_board(board):
    boardHeader = []
    boardHeader.extend(board_top * 6)
    print('  ', end='')
    for i in range(1, 7):
        print(str(i).rjust(20), end="")
    print()
    print('  ', end='')
    for i in boardHeader:
        print(str(i).rjust(2), end='')
    print()

    for x in range(20):  
        board.append(["#"] * board_size)

    row = 0
    for i in range(1, 21):  #row is 20
        print(str(row + 1).rjust(2), end="")
        for j in range(len(board[row])):
            print(board[row][j].rjust(2), end='')
        row += 1
        print()
    return board

# generate random row and column
def random_row(board):
    return randint(1, len(board) - 1)
def random_col(board):
    return randint(1, len(board[0]) - 5) 

def random_ship(board):
    ship_row = random_row(board) #coordinates for the ships
    ship_col = random_col(board)
    return ([ship_row, ship_col])

# generate random ships
def gamemode(x): 
    mainShips = [] #main list for ships
    while len(mainShips) < x: 
        tempShips = [] #temporary list to store ships
        tempShipRand = random_ship(board)
        ships_row = tempShipRand[0]
        ships_col = tempShipRand[1]
        tempShips.append(tempShipRand)
        for j in range(1, 5):   #ships are 5 char long
            tempShips.append([ships_row, ships_col + j])

        dup = False             #compare to find out duplicates
        for k in tempShips:
            for l in mainShips:
                if k in l:
                    dup = True

        if not dup:
            mainShips.append(tempShips)  #add to main list if not duplicate
    return (mainShips)

# loading new game board
def load_game(board):
    print ("\nThe rules is the same. Good Luck!")
    print()
    del board[:]
    print_board(board)
    random_row(board)
    random_col(board)
    random_ship(board)
    
    return {
        'random_row':random_row,
        'random_col':random_col,
        'random_ship':random_ship
    }

# asking for rematch
def rematch():
    rematch = str(input("That was fun right? Wanna play again? (Y/N): "))
    if rematch.lower() == 'y':  #accept rematch
        load_game(board)
        main_game()
    elif rematch.lower() == 'n':   #decline rematch
        print ("That's too bad. Hope to see you soon!")
    else:
        print("Sorry, I dont understand. Please enter again!")
        
# the main codes of the game 
def main_game():
    selection = str(input("Select S to start or ""Q"" to quit "))
    if selection == "s" or selection == "S":
      gamemodeVar = int(input("Select mode: \n(1)Beginner Mode 80 random ships \n(2)Intermediate Mode 50 random ships \n(3)Advanced Mode 20 random ships \n(4)Custom Mode"))
      #Game Mode 1 (Beginner Mode)
      if gamemodeVar == 1:
          gameStats = gamemode(80) #set 80 ships
          mainShips = gameStats
          ships = 5
          booms = 15
          while booms > 0 and ships > 0:
              limit_row = 20
              limit_col = 60
              guess_row, guess_col = map(int, input("Enter coordinates for row and column: eg.(10 14)").split(" ")) #prompt user to enter ship location
              guess_row -= 1
              guess_col -= 1
              hit = False
              if guess_row <= limit_row or guess_col <= limit_col:
                  for group in mainShips:
                      if [guess_row, guess_col] in group:  
                          hit = True
                          print("BOOOOOOOOOOOM! \nWay to go,", "Captain",name)

                          for indCoord in group:
                              board[indCoord[0]][indCoord[1]] = "O"
                          booms -= 1
                          ships -= 1
                          print("You have", booms, "amount of booms left.")
                          print(ships, "ship left")
                          print_board(board)
                          break

                  if not hit:
                      print("You missed Captain", name, "...C'mon!")
                      board[guess_row][guess_col] = " "
                      booms -= 1
                      print("You have", booms, "amount of booms left.")
                      print_board(board)
                      
                  if booms == 3 and ships != 0:
                      clue = input("Do you want any clue? (Y/N) \nNOTE:It'll be random (It may not be worth it if it is the ship you've destroyed) \nY/N?:") #prompt user to accept or reject clue offer
                      if clue == "Y" or clue == "y":
                          print ("Ship_row and ship_col is near", group[0][0], group[0][1])
                      else:
                          print("Good luck then!") 
          
                  if booms == 0:
                      print("You ran out of booms \nYou have no luck today, try again...")
                      rematch()
                      break
                  if ships == 0:
                      print("Congrats, you have destroyed 5 ships")
                      total_attempts = 15 - booms
                      print("Your total attempts is:", total_attempts)
                      rematch()
                      if booms <= 2 and booms >= 0:
                          print("You are a novice, Cap", name)
                      elif booms <= 5 and booms >= 3:
                          print("Not too bad, Cap", name)
                      elif booms > 5:
                          print("You have the talent!, Cap", name)
                      else:
                          print("Invalid coordinate!!")
                          print("You have", booms, "amount of booms left.")
              else:
                  if guess_row > limit_row or guess_col >limit_col:
                      print("Invalid coordinate!!")
                      booms -= 1
                      print("You have", booms, "amount of booms left.")
      #Game Mode 2 (Intermediate Mode)
      elif gamemodeVar == 2:
          gameStats = gamemode(50) #set 50 ships
          mainShips = gameStats
          ships = 5
          booms = 15
          while booms > 0 and ships > 0:
              limit_row = 20
              limit_col = 60
              guess_row, guess_col = map(int, input("Enter coordinates for row and column: ").split(" ")) #prompt user to enter ship location
              guess_row -= 1
              guess_col -= 1
              hit = False
              if guess_row <= limit_row or guess_col <= limit_col:
                  for group in mainShips:
                      if [guess_row, guess_col] in group:  
                          hit = True
                          print("BOOOOOOOOOOOM! \nWay to go,", "Captain",name,"!!!")

                          for indCoord in group:
                              board[indCoord[0]][indCoord[1]] = "O"
                          booms -= 1
                          ships -= 1
                          print("You have", booms, "amount of booms left.")
                          print(ships, "ship left")
                          print_board(board)
                          break

                  if not hit:
                      print("You missed Captain", name, "...C'mon!")
                      board[guess_row][guess_col] = " "
                      booms -= 1
                      print("You have", booms, "amount of booms left.")
                      print_board(board)

                  if booms == 4 and ships != 0:
                      clue = input("Do you want any clue? (Y/N) \nNOTE:It'll be random (It may not be worth it if it is the ship you've destroyed) \nY/N?:") #prompt user to accept or reject clue offer
                      if clue == "Y" or clue == "y":
                          print ("Ship_row and ship_col is near", group[0][0], group[0][1])
                      else:
                          print("Good luck then!")     

                  if booms == 0:
                      print("You ran out of booms \nYou have no luck today, try again...")
                      rematch()
                      break
                  if ships == 0:
                      print("Congrats, you have destroyed 5 ships")
                      total_attempts = 15 - booms
                      print("Your total attempts is:", total_attempts)
                      rematch()
                      if booms <= 2 and booms >= 0:
                          print("You are a novice, Cap", name)
                      elif booms <= 5 and booms >= 3:
                          print("Not too bad, Cap", name)
                      elif booms > 5:
                          print("You have the talent!, Cap", name)
              else:
                  if guess_row > limit_row or guess_col >limit_col:
                      print("Invalid coordinate!!")
                      booms -= 1
                      print("You have", booms, "amount of booms left.")
                   
      # Game Mode 3 (Advanced Mode)
      elif gamemodeVar == 3:
           gameStats = gamemode(20) #set 20 ships
           mainShips = gameStats
           ships = 5
           booms = 15
           while booms > 0 and ships > 0:
              limit_row = 20
              limit_col = 60
              guess_row, guess_col = map(int, input("Enter coordinates for row and column: ").split(" "))  #prompt user to enter ship location
              guess_row -= 1
              guess_col -= 1
              hit = False
              if guess_row <= limit_row or guess_col <= limit_col:
                  for group in mainShips:
                      if [guess_row, guess_col] in group:  
                          hit = True
                          print("BOOOOOOOOOOOM! \nWay to go,", "Captain",name,"!!!")
                          for indCoord in group:
                              board[indCoord[0]][indCoord[1]] = "O"
                          booms -= 1
                          ships -= 1
                          print("You have", booms, "amount of booms left.")
                          print(ships, "ship left")
                          print_board(board)
                          break

                  if not hit:
                      print("You missed Captain", name, "...C'mon!")
                      board[guess_row][guess_col] = " "
                      booms -= 1
                      print("You have", booms, "amount of booms left.")
                      print_board(board)

                  if booms == 5 and ships != 0:
                      clue = input("Do you want any clue? (Y/N) \nNOTE:It'll be random (It may not be worth it if it is the ship you've destroyed) \nY/N?:") #prompt user to accept or reject clue offer
                      if clue == "Y" or clue == "y":
                          print ("Ship_row and ship_col is near", group[0][0], group[0][1])
                      else:
                          print("Good luck then!") 

                  if booms == 0:
                      print("You ran out of booms \nYou have no luck today, try again...")
                      rematch()
                      break
                  if ships == 0:
                      print("Congrats, you have destroyed 5 ships")
                      total_attempts = 15 - booms
                      print("Your total attempts is:", total_attempts)
                      rematch()
                      if booms <= 2 and booms >= 0:
                          print("You are a novice, Cap", name)
                      elif booms <= 5 and booms >= 3:
                          print("Not too bad, Cap", name)
                      elif booms > 5:
                          print("You have the talent!, Cap", name)
                      else:
                          print("Invalid coordinate!!")
                          print("You have", booms, "amount of booms left.")
              else:
                  if guess_row > limit_row or guess_col >limit_col:
                      print("Invalid coordinate!!")
                      booms -= 1
                      print("You have", booms, "amount of booms left.")
# Game Mode 4, Customising your own ship!
      elif gamemodeVar == 4:
           y = int(input("Enter the amount of ships you would like to have on the board: \nMinimum 1 ship and Maximum 150 ships "))
           while y <= 0 or y > 150:
               y = int(input("Invalid amount of ships! Please enter again: "))
           ships = int(input("Enter the amount of ships you would like to destroy to win: "))
           while ships > y or ships <= 0:
               ships = int(input("You've either entered more amount of ships to destroyed than the ships you have on the board or you've entered ships lesser than 1. Please enter again: "))
           booms = int(input("Enter the amount of booms you would like to have: "))
           gameStats = gamemode(y)
           mainShips = gameStats
           while booms > 0 and ships > 0:
               limit_row = 20
               limit_col = 60
               guess_row, guess_col = map(int, input("Enter coordinates for row and column: eg.(10 14) ").split(" "))  #prompt user to enter ship location
               guess_row -= 1
               guess_col -= 1
               hit = False
               if guess_row <= limit_row or guess_col <= limit_col:
                 for group in mainShips:
                     if [guess_row, guess_col] in group:  
                         hit = True
                         print("BOOOOOOOOOOOM! \nWay to go,", "Captain",name,"!!!")
                         for indCoord in group:
                             board[indCoord[0]][indCoord[1]] = "O"
                         booms -= 1
                         ships -= 1
                         print("You have", booms, "amount of booms left.")
                         print(ships, "ship left")
                         print_board(board)
                         break

                 if not hit:
                     print("You missed Captain", name, "...C'mon!")
                     board[guess_row][guess_col] = " "
                     booms -= 1
                     print("You have", booms, "amount of booms left.")
                     print_board(board)
          
                 if booms == 5 and ships != 0:
                     clue = input("Do you want any clue? (Y/N) \nNOTE:It'll be random (It may not be worth it if it is the ship you've destroyed) \nY/N?:") #prompt user to accept or reject clue offer
                     if clue == "Y" or clue == "y":
                         print ("Ship_row and ship_col is near", group[0][0], group[0][1])
                     else:
                         print("Good luck then!") 

                 if booms == 0:
                     print("You ran out of booms \nYou have no luck today, try again...")
                     rematch()
                     break
                 if ships == 0:
                     print("Congrats, you have destroyed all the ships!")
                     rematch()
               else:
                   print("Invalid coordinate!!")
                   print("You have", booms, "amount of booms left.")
      
    else: 
        selection.lower() == "q"  #Enter 'Q/q' for Quit
        print ("You don't really want to play, do you?")
        exit = True
          
print("                            __ ___ _ __ _ _ _      ")
print("                           / - /_ ___ __ - -       ")
print("                __________||_||____                ")
print("                \     CSC1024     /                ")
print("~~~~~~~~~~~~~~~~~\_______________/~~~~~~~~~~~~~~~~~")
print("")
print ("{:>45}".format("Welcome to Battleship game!\n"))
name = input("Enter your name, Captain: ")
print("Welcome on board, Captain", name, "\nThe RULES are simple: You must eliminate 5 ships to win.")
print("LET'S DO IT!")
print_board(board)  
main_game()
