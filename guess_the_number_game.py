"""
Final Project: Guess the Number Game
===========================
Student:  Theresa Fu-Hsing Hsu
Semester: Spring 2023
Course: CS 5001
"""

import random


def main():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of tries
    num_tries = 0
    
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    
    # Loop until the player guesses the number or runs out of tries
    while num_tries < 10:
        guess = int(input("Enter your guess: "))
        num_tries += 1
        
        if guess < 1 or guess > 100:
            print("Your guess is out of range. Please enter a number between 1 and 100.")
        elif guess < secret_number:
            print("Too low. Try again.")
            if num_tries == 2:
                hint_low = guess
                hint_high = 100
                print("Hint: The number is between {} and {}.".format(hint_low, hint_high))
        elif guess > secret_number:
            print("Too high. Try again.")
            if num_tries == 2:
                hint_low = 1
                hint_high = guess
                print("Hint: The number is between {} and {}.".format(hint_low, hint_high))
        else:
            print(f"Congratulations! You guessed the number in {num_tries} tries.")
            return
    
    print(f"Sorry, you ran out of tries. The number was {secret_number}.")
    

def computer_plays():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of tries
    num_tries = 0
    
    # Initialize the guessing range
    low = 1
    high = 100
    
    # Loop until the computer guesses the number
    while True:
        guess = (low + high) // 2
        num_tries += 1
        
        print(f"The computer's guess is {guess}.")
        
        if guess < secret_number:
            print("Too low. The computer will try again.")
            low = guess + 1
            hint_low = guess + 1
            hint_high = high
            print("Hint: The number is between {} and {}.".format(hint_low, hint_high))
        elif guess > secret_number:
            print("Too high. The computer will try again.")
            high = guess - 1
            hint_low = low
            hint_high = guess - 1
            print("Hint: The number is between {} and {}.".format(hint_low, hint_high))
        else:
            print(f"The computer guessed the number in {num_tries} tries.")
            return
    

if __name__ == '__main__':
    play_mode = input("Enter '1' to play the game yourself, or '2' for the computer to play: ")
    
    if play_mode == '1':
        main()
    elif play_mode == '2':
        computer_plays()
    else:
        print("Invalid input. Please enter either '1' or '2'.")
