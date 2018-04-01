#Make a two-player Rock-Paper-Scissors game.
#(Hint: Ask for player plays (using input),
#compare them, print out a message of congratulations to the winner,
#and ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock
import random

winning = {"rock":"scissors", "scissors":"paper", "paper":"rock"}
select = ["rock", "paper", "scissors"]
Game = True

def player_choice():
    game_mode = raw_input("""Choose your game mode:\n \n
    1. Human vs Superior CPU technology \n
    2. Human vs Human \n
    3. Battle of Redundancy: """)
    print(game_mode, type(game_mode))
    if game_mode not in ['1','2','3']:
        return player_choice()
    elif game_mode == '1':
        return pvc()
    elif game_mode == '2':
        pvp()
    elif game_mode == '3':
        cvc()


def pvc():
    Game = True    
    while Game == True:
        player1 = raw_input("What do you choose? ")
        player2 = random.choice(select)
        if winning[player2] ==  player1:
            print(player2 + " beats " + player1 + "computer wins")
        elif player2 == player1:
            print(" It's a Tie! ")
        else:
            print(player1 + " always beats " + player2 + "; player 1 wins")

        again = raw_input("Do you want to play again? y/n ")
        
        if again == "y":
            player_choice()
        else:
            Game = False
            return "Goodbye, sore loser"

def pvp():
    Game = True
    while Game == True:
        player1 = raw_input("What do you choose? ")
        player2 = raw_input("And your choice?")
        if winning[player2] ==  player1:
            print(player2 + " beats " + player1 + "computer wins")
        elif player2 == player1:
            print(" It's a Tie! ")
        else:
            print(player1 + " always beats " + player2 + "; player 1 wins")

        again = raw_input("Do you want to play again? y/n ")
        
        if again == "y":
            player_choice()
        else:
            Game = False
            return "You both suck Peace"

def cvc():
    Game = True
    while Game == True:
        player1 = random.choice(select)
        player2 = random.choice(select)
        if winning[player2] ==  player1:
            print(player2 + " beats " + player1 + "computer wins")
        elif player2 == player1:
            print(" It's a Tie! ")
        else:
            print(player1 + " always beats " + player2 + "; player 1 wins")

        again = raw_input("Do you want to play again? y/n ")
        
        if again == "y":
            player_choice()
        else:
            Game = False
            return "Like life, No One really wins"


player_choice()