import random

while True:
    # initiating computer choices of Rock, Paper and Scissors
    com_choices = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(com_choices)
    
    # initiating player choices of 'r' for Rock, 'p' for Paper and 's' for Scissors
    player_choices = ['r','p','s']
    print(computer)
    
    player = None
    
    # verifies that player inputs the right choices
    while player not in player_choices:
        player = input("Enter R for Rock or P for Paper or S for Scissors?: ").lower()
        
    if player == 'r':
        player = 'Rock'
        
    elif player == 'p':
        player = 'Paper'
       
        
    elif player == 's':
        player = 'Scissors'
        
    # Condition for tie    
    if player == computer:
        print("player"  + "("+ player + ")")
        print("computer " + "("+ computer +")")
        print("Tie!")
    
    # Condition for Win/lose  
    elif player == "Rock":
        if computer == "Paper":
            print("player"  + "("+ player + ")")
            print("computer " + "("+ computer +")")
            print("You lose!")
        if computer == "Scissors":
            print("player"  + "("+ player + ")")
            print("computer " + "("+ computer +")")
            print("You win!")
    
    elif player == "Scissors":
        if computer == "Rock":
            print("player"  + "("+ player + ")")
            print("computer " + "("+ computer +")")
            print("You lose!")
        if computer == "Paper":
            print("player"  + "("+ player + ")")
            print("computer " + "("+ computer +")")
            print("You win!")
            
    elif player == "Paper":
        if computer == "Scissors":
            print("player"  + "("+ player + ")")
            print("computer " + "("+ computer +")")
            print("You lose!")
        if computer == "Rock":
            print("player"  + "("+ player + ")")
            print("computer " + "("+ computer +")")
            print("You win!")
            
    # asks if the user wants to play again     
    play_again = input("play again? (yes/no): ? ").lower()
        
    if play_again != "yes":
            break
print("bye!")

    