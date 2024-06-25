# Create a function that will run all the code to run the game as expected. You should begin by creating a new script called milestone_5.py. Copy all the codes in milestone_4.py file into the newly created milestone_5.py file.


# Step 1:
# Create a function called play_game that takes word_list as a parameter. Inside the function, write the code for the following steps

# Create a variable called num_lives and assign it to 5
# Create an instance of the Hangman class. Do this by calling the Hangman class and assign it to a variable called game
# Pass word_list and num_lives as arguments to the game object
# Create a while loop and set the condition to True. In the body of the loop, do the following:
# Check if the num_lives is 0. If it is, that means the game has ended and the user lost. Print a message saying 'You lost!'
# Next, check if the num_letters is greater than 0. In this case, you would want to continue the game, so you need to call the ask_for_input method.
# If the num_lives is not 0 and the num_letters is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'
# Step 2:
# Outside the function, call your play_game function to play your game. Don't forget to pass in your list of words as argument to the function.

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
                    if guess==self.letters[i]:
                        self.word_guessed[i]=guess
                self.num_letters-=1
            else:
                # Reduce `num_lives' by 1
                self.num_lives-=1
                print("Sorry, {letter} is not in the word.")
                print(f"You have {self.num_lives} lives left.")



    
    def ask_for_input(self):
        
        guess = input("Enter a letter:")
        if len(guess) != 1 or guess.isalpha() == False:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters>0:
            print(game.word_guessed)
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

play_game(["banana", "dates", "apple", "orange", "grapes"])
