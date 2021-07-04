#write a function that takes a list and return a new list with unique elements of the first list

def unique_list(lst):

    return list(set(lst))

lst=input('Please enter a sentance')
print(unique_list(lst))