#write a function that checks whether a string is a pangram or not

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    anonymous=[]
    new_anonymous=''

    for word in str1.split():
        for letter in word.lower():
            anonymous+=letter

    for a in sorted(set(anonymous)):
        new_anonymous+=a
    return new_anonymous==alphabet
sentence=input('Please enter a sentance or a word to check it is Pangram: ')
print(ispangram(sentence))