#sandygcabanes
#w3resources.com
#mini project 3 guess a number
''' Create a Python project to guess a number that the computer selected'''

import random
chosen_number = int(random.randint(1,100))
print (chosen_number)

n = 1
def guess_the_number ():
    global n
    guess_ = int(input('Guess the number between 1 and 100:'))
    if guess_ == chosen_number:
        print ('Correct.  You have made {} guesses.'.format(n))
    elif guess_ != chosen_number:
        if guess_ > chosen_number:
            print ('Guess lower')
        if guess_ < chosen_number:
            print ('Guess higher')
        n += 1
        guess_the_number()
guess_the_number()



