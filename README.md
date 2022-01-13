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


The description of the game: 

In this Battleship Game, the main purpose is for the users to successfully ‘boom’ a specific amount of randomly generated ships within a specific number of attempts. For Game Mode 1 (Beginner), Game Mode 2 (Intermediate) and Game Mode 3 (Advanced), the number of ships generated on the board is 80, 50 and 20 respectively. Meanwhile, there are several added game features which are custom mode, clues, rematch, name of user, human-like prompts, and logo of the game to give users an amazing experience playing.

The custom mode game is named as Game Mode 4. In this game mode, users are able to customize the number of ships from 1 to 150, the number of ships (5 characters long) they would like to destroy as well as the number of booms they desire on the same board length. This is to make the game more interesting for the users to play rather than only playing the default modes. For instance, the users can set a board with 150 ships and attempting to destroy only one ship with 100 booms.

Furthermore, offering random clue of the location of a ship to users is prompted according to the different game modes. For example, in Game Mode 1 (Beginner), when users are left with 3 booms, the users can choose whether to accept or decline the random clue. This applies the same to Game Mode 2 and 3 with different number of booms left. This feature encourages the users to keep playing to win. 

Another unique feature in the game is allowing users to play again if they want a rematch. It is more convenient for users as they do not need to click “Run” every single time when they want a rematch after they won or lost.  

In the beginning of the game, users are required to enter their preferred name. Their name would be called certain times like when they miss the shot. For instance, "You missed Captain _______, C'mon!" This feature improves user interactivity with the program that results in users feeling more connected than ever.

Moreover, the game uses human-like prompts to interact with users as they play the game. For instance, “BOOOOOOOOOOOM! Way to go Captain _____!!!” when users managed to hit a ship or “You don’t really want to play, do you?” when users want to quit playing. In the former, users will feel motivated but, in the latter, there is a sense of sarcasm in challenging users to not quit the game, thus, making things more fun. Users will also feel more engaged as they are able to relate to the layman’s terms used in the game. In short, the prompts given are not complex and users without programming knowledge would know what the prompts mean.

Just like any other games, there will always be a unique signature. For this game, the game logo is printed out in the beginning of the game with an image of a ship with the code CSC 1024. This feature beautifies the game and will also help to differentiate this game from other games. 
