#write a function that checks whether a word or a phrase is palindrome or Not

def palindrome(s):
    s=s.lower()
    a=s.replace(' ','')

    return a==a[::-1]

s=input('Enter a Word or Phrase: ')
print(palindrome(s))