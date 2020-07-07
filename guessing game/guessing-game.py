import random
from variables import number_of_guesses
from variables import correct_answer

# Game setup
print('Welcome to the number guessing game!')


while number_of_guesses > 0:
    # User guesses the number
    user_guess = input('Guess a number between 1 and 10: ')
    # overwrites the user guess variable with the integer value
    user_guess = int(user_guess)

    # Computer tells the user whether the guess was too high or too low
    if user_guess == correct_answer:
        print('good guess')
        print('You are correct!')
        user_won = True
        break
    elif user_guess > correct_answer:
        print('Sorry, you guessed too high!')
    elif user_guess < correct_answer:
        print('Sorry, you guessed too low!')

    number_of_guesses -= 1

if user_won == True:
    print('You Win!')
else:
    print('You Lose!')
