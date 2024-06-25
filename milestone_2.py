import random

word_list = ["banana", "dates", "apple", "orange", "grapes"]
word = random.choice(word_list)


print(word)

guess = input("Enter a letter:")
if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")