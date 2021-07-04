# write a function to multiply all the numbers in a list

def multiply(numbers):
    number = 1
    for b in numbers:
        number *= b
    return number

lst = [2, 3, 4, 5, 6, 7]
print(multiply(lst))