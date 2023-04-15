import random  # Importing random so the program can select a random number between 0 and the set value.

print('Welcome to the number guessing game!\n\nHave a go and try to')   # Greeting to the game.


def no_to_find(x):  # Defining guess
    random_number = random.randint(1, x)  # Chooses the number that needs to be found.
    guess_no = 0
    while guess_no != random_number:  # If the correct number hasn't been chosen yet this allows the program to loop.
        guess_no = int(input(f'Guess a number between 1 and {x}\n: '))
        if guess_no < random_number:  # If the guess is below the random number this will print.
            print('Too low, Guess again.')
        elif guess_no > random_number:  # If the guess is above the random number this will print.
            print(' Too high., Guess again.')

    print(f'Good work, You guessed the number {random_number} correctly.')  # When the correct number has been guessed
                                                                            # this will print.


no_to_find(1000)  # This sets the guessing number range.
