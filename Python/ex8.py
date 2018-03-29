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


while Game == True:
    player1 = raw_input("What do you choose? ")
    player2 = random.choice(select)
    if winning[player2] ==  player1:
        print(player2 + " beats " + player1)
    elif player2 == player1:
        print(" It's a Tie! ")
    else:
        print(player1 + " always beats " + player2)

    Game = False
