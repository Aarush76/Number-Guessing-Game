import random 

number = random.randint(1,9)
guess = int(input('A number between one and nine has been chosen.\nYou have 5 turns to guess the number.\nEnter your guess :'))
turns = 0

while True:
        
    if number == guess:
        print('YOU WON !!')
        break

    elif turns == 5:
        print("YOU LOSE !! The number was " + number)
        break

    else:
        if number > guess:
            print('Too Low')
        else:
            print('Too High')

        print(f'You have {5-turns} guesses left.')
        turns += 1
        guess = int(input('Guess again : '))
