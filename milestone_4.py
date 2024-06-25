# Create a new script called milestone_4.py. This file will contain the code for the third milestone.

# Define the __init__ method of the Hangman class.


# Step 1:
# Create a class called Hangman.


# Step 2:
# Inside the class, create an __init__ method to initialise the attributes of the class.

# Pass in word_list and num_lives as parameters. Make num_lives a default parameter and set the value to 5.


# Step 3:
# Initialise the following attributes:

# word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
# word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
# num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
# num_lives: int - The number of lives the player has at the start of the game.
# word_list: list - A list of words
# list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially


# Step 1:
# Define a method called check_guess. Pass the guess to the method as a parameter. In the body of the method, write the code for the following steps:

# Convert the guessed letter to lower case
# Create an if statement that checks if the guess is in the word
# In the body of the if statement, print a message saying "Good guess! {guess} is in the word."
# You will continue with the logic of the check_guess method in the next task. For now, let's create the ask_for_input method.


# Define what happens if the guess is not in the word you are trying to guess.

# Step 1:
# In the check_guess method, Create an else statement.


# Step 2:
# Within the else block:

# Reduce `num_lives' by 1
# Print a message saying "Sorry, {letter} is not in the word."
# Print another message saying "You have {num_lives} lives left."

import random
import re

class Hangman:
    def __init__(self, word_list, num_lives=5):

       
        self.word = [i.split(" ") for i in random.choice(word_list)]
        self.word_guessed = ['_' for i in range(0, len(self.word))]
        self.letters = [i[0] for i in self.word]
        self.num_letters = len(set( self.letters))
        self.num_lives = num_lives
        self.word_list = word_list
        # self.word_guessed = re.sub(r'[a-zA-Z]', '_', self.word)
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in self.letters:
                print(f"Good guess! {guess} is in the word")
                for i in range(0, len(self.letters)):
                    if guess==i:
                        self.word_guessed[i]=guess
                self.num_letters-=1
            else:
                # Reduce `num_lives' by 1
                self.num_lives-=1
                print("Sorry, {letter} is not in the word.")
                print(f"You have {self.num_lives} lives left.")



    
    def ask_for_input(self):
        game = True
        while game:
            guess = input("Enter a letter:")

            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)



hangman = Hangman(["banana", "dates", "apple", "orange", "grapes"])
print(hangman.word_guessed)
print(hangman.word)
print(hangman.num_letters)
hangman.ask_for_input()