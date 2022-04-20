'''
Name: Myrisa Mitchell
Date: 04/01/22

This program will prompt a user to guess a randomly selected number until
they get it correctly.

Step 1: Ask for player's name
Step 2: Greet player
Step 3: Generate random number between 1-20
Step 4: Ask player to guess the random number
Step 5: Have player repeat guess until they get it
Step 5a: Inform player if their guess is too high or too low
Step 5b: If player guesses within 6 tries, they win the game
Step 5c: If the play doesn't guess within 6 tries, they lose the game
Step 6: Once game is over, inform player whether they won or lost 
Step 6a: Reveal the number.
'''

import random 

#Step 1
def input_name():
    print(f"Welcome to the -- Guess the Number -- game!")
    firstname = input("What is your name? ")
    return firstname
    
#Step 2
def greet_player(first_name):
    print(f"Hello, {first_name}. I am thinking of a whole number between 1 and 20.")
    print(f"You get 6 tries to guess the number.")

def guess_number():
    games_won = 0
    games_lost = 0
    #Step 3
    number = random.randint(1,20)
    #Step 4
    guesses = 0
    guessed = False
    #Step 5
    while (guesses < 6 and not guessed):
        guesses += 1
        guess = int(input("Take a guess: "))
        #Step 5a
        if (guess > number):
            print(f"That guess is too high. Try again.")
            continue
        elif (guess < number): 
            print("That guess is too low. Try again.")
            continue
        else:
            #Step 5b
            print("Congratulations! You've guessed the number.")
            guessed = True
    else: 
        #Step 5c
        print("Sorry, you've taken too many tries to guess the number.")

    #Step 6
    if (guess == number):
        games_won += 1
        if (guesses == 1):
            print(f"Well done! You guessed my number in {guesses} try!")
        else:
            print(f"Well done! You guessed my number in {guesses} tries!")
    else:
        games_lost += 1
        #Step 6a
        print(f"My number was {number}. Maybe next time!")
    return games_won, games_lost

def play_again():
    again = input("Would you like to play again? [Enter y/n]: ")
    if (again == "y"):
        return True
    return False
    #     guess_number()
    #     play_again()
    # else:
    #     print(f"Okay, see you next time!")

def main():
    runagain = True 
    first_name = input_name()
    greet_player(first_name)
    while (runagain):
        guess_number()
        play_again()
        if play_again() == False:
            runagain = False

    games_stats = guess_number()
    print(f"You won {games_stats[0]} games.")
    print(f"You lost {games_stats[1]}.")
        
if __name__ == "__main__":
    main()