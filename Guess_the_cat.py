# Guess the cat

from random import shuffle


def list_shuffle(mylist):
    shuffle(mylist)

    return mylist


def guess():
    a = ''

    while a not in ['0', '1', '2']:
        a = input('Enter the place: 0, 1 or 2: ')

    return int(a)


def check_guess(my_guess):
    if newlist[my_guess] == 'cat':

        print('Correct')

        print(newlist)

    else:

        print('Wrong Guess!')

        print(newlist)


# define the list

mylist = ['cat', 'dog', 'cow']

# suffle the list

newlist = list_shuffle(mylist)

# guess the place of cat

my_guess = guess()

#print(my_guess)


# check guess

check_guess(my_guess)
