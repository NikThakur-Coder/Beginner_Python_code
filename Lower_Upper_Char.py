#write a function that accepts a string and calculates the number of upper case letters and lower case letters

def up_low(s):
    upper=0
    lower=0
    for word in s.split():
        for letter in word:
            if letter.isupper():
                upper+=1
            elif letter.islower():
                lower+=1

    return f'No. of Upper case characters: {upper} \nNo. of Lower case characters: {lower}'

string=input('Please Enter a String: ')
print(up_low(string))