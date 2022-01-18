"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    guess = 0
    attempts = 0

    print("Welcome to number guessing game")

    number = random.randint(1, 10)
    
    while guess != number:
        try:
            guess = int(input("Pick a number 1-10: "))
            attempts += 1
        except ValueError as err:
            print("Input must be between 1 and 10")
            print("Sorry, try again")

    # http://inventwithpython.com/chapter4.html             
        if guess == number:
            print("You got it! It took you {} tries, game over".format(attempts))

        if guess > number:
            print("Sorry, too high")
        
        if guess < number:
            print("Sorry, too low")

    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()