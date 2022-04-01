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
    #Step 3
    number = random.randint(1,20)
    #Step 4
    guesses = 0
    #Step 5
    while (guesses < 6):
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
            break
    else: 
        #Step 5c
        print("Sorry, you've taken too many tries to guess the number.")

    #Step 6
    if (guess == number):
        if (guesses == 1):
            print(f"Well done! You guessed my number in {guesses} try!")
        else:
            print(f"Well done! You guessed my number in {guesses} tries!")
    else:
        #Step 6a
        print(f"My number was {number}. Maybe next time!")

def play_again():
    again = input("Would you like to play again? [Enter y/n]: ")
    if (again == "y"):
        guess_number()
        play_again()
    else:
        print(f"Okay, see you next time!")

def main():
    first_name = input_name()
    greet_player(first_name)
    guess_number()
    play_again()
        
if __name__ == "__main__":
    main()