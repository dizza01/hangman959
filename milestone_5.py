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


if __name__ == '__main__':
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
