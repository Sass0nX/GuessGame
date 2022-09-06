ezer = 0
while ezer == 0:
    ranges = range(2, 50, 1)
    range_list = list(ranges)
    lucky_numbers = [25, 8, 19, 7, 43]  # List of lucky numbers
    guesses = []  # Create a list
    print("""Welcome to 'Guess Game'!
    you need to guess five numbers between 2-49 and you have 20 chance to guess All,
    if you enter the same number TWICE you lose
    Good Luck!!!!!!!!!!""")
    print('_________________________________________________')
    for i in range(20, 0, -1):  # For Loop that run 20 times
        x = 20 - i  # x = 20 - i to get the number of number to success
        guess = int(input('guess a number: '))  # input number and store him in vairable guess
        guesses.append(guess)  # push the guess to the list
        if i - 1 == 0:
            ezer = 0
            print('------------------------------')
            print('''

        You Lost The Game!''')
        if guess not in range_list:
            print(f'The number {guess} is out of the rage, u left only {i - 1} guesses')
            continue
        if guesses.count(guess) >= 2:  # if the list contain same number more than 1 time break the loop
            print('You guessed the same number twice, you lose the game, Try again')
            ezer = 1
            break
        if lucky_numbers.count(guess) == 1:  # if the guessed number in the list go into loop
            lucky_numbers.remove(guess)  # remove the number if in the list and guessed right
            print(f'you guess a number!, you left only {i - 1} guesses!')
            if len(lucky_numbers) == 0:  # if length of list 0 the game is over
                print(f'!!!!!Congratulation u guessed all the numbers, you use only {x + 1} guesses!!!!!')
                ezer = 1
                break
        else:
            print(f'bad guess!, you left only {i - 1} guesses!')
