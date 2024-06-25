
# class milestone_2:
#     def __init__(self):

#         self.word_list = ["banana", "dates", "apple", "orange", "grapes"]
#         print(word_list) 


# To accomplish this task, you will need to use the 'random' module.
# The random module is one of Python's built-in modules.
# It has a choice method which returns a random item from a given sequence.


# Step 1:
# Go to the first line of your file.


# Step 2:
# Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.


# Step 3:
# Create the random.choice method and pass the word_list variable into the choice method.


# Step 4:
# Assign the randomly generated word to a variable called word.


# Step 5:
# Print out word to the standard output. Run the code several times and observe the words printed out after each run.



import random

word_list = ["banana", "dates", "apple", "orange", "grapes"]
word = random.choice(word_list)


word_list = ["banana", "dates", "apple", "orange", "grapes"]
word = random.choice(word_list)
letter_lst = [i[0].split(" ") for i in word]

letters = [i[0] for i in letter_lst]

print(letter_lst)

# In this task, you are required to take user input. As you now know, the print() function in Python displays output on the screen. Conversely, Python has an input() function that takes input from the screen. Note that the input function returns the user input in form of a string.


# Step 1:
# Using the input function, ask the user to enter a single letter.


# Step 2:
# Assign the input to a variable called guess.


# Usually, when taking input from users, it is best to validate that the input makes sense.
# For example, we may want to ensure that only a single letter is entered and that only alphabetical characters are provided by the user.
# To do this, create conditional checks that must be passed before the input can be accepted.


# Step 1:
# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.


# Step 2:
# In the body of the if statement, print a message that says "Good guess!".


# Step 3:
# Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.




# guess = input("Enter a letter:")
# if len(guess) == 1:
#     print("Good guess!")
# else:
#     print("Oops! That is not a valid input.")