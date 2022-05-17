'''
Name: Myrisa Mitchell
Date: May 2, 2022

This program will play the game of hangman, continuing until the player no longer wants to play.
Functions:
1. Create board
2. Choose random word
3. Greet Player
4. Guess word
5. Play game
6. Play again?


'''
from sys import *
import random 

def board():
    #This function builds the board in stages
    stage_0 = "|__________\n|/     |\n|\n|\n|\n|\n|\n-------------\n"
    stage_1 = "|__________\n|/     |\n|      O\n|\n|\n|\n-------------\n"
    stage_2 = "|__________\n|/     |\n|      O\n|      |\n|      |\n|\n|\n-------------\n" 
    stage_3 = "|__________\n|/     |\n|      O\n|     \|\n|      |\n|\n|\n-------------\n"
    stage_4 = "|__________\n|/     |\n|      O\n|     \|/\n|      |\n|\n|\n-------------\n" 
    stage_5 = "|__________\n|/     |\n|      O\n|     \|/\n|      |\n|     /\n|\n-------------\n"
    stage_6 = "|__________\n|/     |\n|    (x x)\n|      -\n|     \|/\n|      |\n|     / \\\n|\n-------------\n"
    stages = [stage_0,stage_1,stage_2,stage_3,stage_4,stage_5,stage_6]
    return stages

def choose_word():
    #This function chooses a random word from the file of words
    words = []
    with open("Assignments/final/words.txt") as fin:
        words = fin.read()
    word_list = words.split()
    game_word = random.choice(word_list)
    return game_word

def greet_player():
    #This function greets the player before theey play the game
    player_name = input("Hi! What is your name? ").capitalize()
    print(f'Hi {player_name}. Welcome to Hangman!')

def guess_word(stages, display, game_word):
    guessed = False
    #This is the bulk of the game. Replaces characters guessed correctly and keeps track of stages
    missed_letters = []
    trials = 0 
    print(f"Try to guess the secret word!")
    while trials != 6:
        print(f'{stages[trials]}')
        print(*display)
        print(f"Missed letters: {' '.join(missed_letters)}")
        guess = input("Guess a letter: ").lower()
        #Replaces letters with guesses
        if guess.isalpha() and len(guess) == 1:
            if guess in game_word:
                for i, ch in enumerate(game_word):
                    if guess == ch:
                        display[i] = guess
            elif guess in missed_letters:
                print("You already guessed this letter.\nTry again.")
            else:                    
                trials += 1
                missed_letters.append(guess)
                if trials < 6:
                    print(f"Try again.")
                if trials == 6:
                    break
        else:
            print("Please use a single letter from the alphabet.")
        if display == list(game_word):
            guessed = True
            print(' '.join(display))
            print(f"Congratulations! You guessed the word.")
            break
    #Lost game
    if (trials == 6):
        print(stages[6])
        print(f"Oh no! You hung hangman.\nThe word was {game_word}.")
    return guessed


def play_again():
    play = False
    #Asks the player if they want to play again
    play_more = input("Would you like to play again? Enter Y/N: ").lower()
    if play_more == 'y':
        play = True 
    elif play_more == 'n':
        print('Okay! See you next time!')
    else:
        print("Please enter 'Y' or 'N'.")
        play_again()
    return play


def main():
    games_won = 0
    games_played = 1
    hangman = True
    greet_player()
    while hangman:
        stages = board()
        game_word = choose_word()
        #Create display
        display = []
        for i in range(len(game_word)):
            display.append('_')
        guessed = guess_word(stages, display, game_word)
        if guessed == True:
            games_won += 1
        play = play_again()
        if play == True:
            games_played += 1
        else:
            #Displays game stats
            print(f"You won {games_won} games and played {games_played} games. Great job!")
            hangman = False

if __name__ == "__main__":
    main()
