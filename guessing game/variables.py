import random

number_of_guesses = 3  # User has 3 guesses before losing the game
user_won = False
# Computer guesses a random number between 1 and 10
correct_answer = random.randint(1, 10)