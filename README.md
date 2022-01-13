# Battleship
A battleship game created for an assignment. This program was co-created among 5 members. 

The assignment had many requirements such as: 
 1. The mission of the player is to eliminate the battleships of their opponent. 
 2. The game should have a 20 rows x 60 columns size, which you should mask the area with ‘#’ characters. 
 3. The game should allow player to choose among 3 stages of difficulties. For example: 
    
     Beginner: 80 ships
     
     Intermediate: 50 ships 
     
     Advance: 20 ships 
     
     Each ship should be in length of 5 characters. 
 4. The location of all ships should be random and should not be visible to the 
        a.player. 
 5. The player is required to choose the location to boom by entering coordinates (row, col). The program should validate the coordinates entered to ensure they are valid. 
 6. Unmask the location which has been boomed. If there’s a ship at that location, unmask the whole ship. 
 7. Each player begins with 15 booms. The screen should display the number of boom left as the game progresses. 
 8. Game will end when player successfully destroyed 5 ships without exhausted all their booms. The screen should display the total number of attempts the player has taken, and show the appropriate ending message, for example:
    
    If total attempts between 13-15: display “You are a novice” 
    
    If total attempts between 10-12: “Not too bad”
    
    If total attempts < 10: “You have the talent!” 
    
 9. Or, game will end if player not able to destroy 5 ships and has no remaining booms. The screen should display the message “You’ve no luck today, try again.” 
