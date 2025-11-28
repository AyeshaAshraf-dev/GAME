
# building a game rock paper scissors yeah :)

import random

options = ("rock", "paper", "scissors") 
player = None
 
playagain = 'Y'

while playagain == 'Y': 
    computer = random.choice(options)
    player = input("Enter a choice(rock, paper, scissors): ")
    if player not in options:
        print("enter a valid choice! ")
        exit()
    print(f"player: {player}")
    print(f"computer: {computer}")
    if player == computer:
        print("its a tie🙂")     
    elif player == "paper" and computer == "rock":
        print("you win! ")     
    elif player == "scissors" and computer == "paper":
        print("you lose! ")     
    elif player == "rock" and computer == "scissors":
        print("you win! ")     
    else:
        print("you lose!")
    playagain = input("\nWant to playagain?\n Enter Y for yes\n       Q for quit\n")

    if playagain == "Q":
        print("\n THANK U FOR PLAYING")

    
