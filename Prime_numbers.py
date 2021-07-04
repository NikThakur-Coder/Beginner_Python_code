#Prime numbers from 2 to user input
def is_prime(num):
    # to check 0 & 1
    if num < 2:
        return 0
    primes = [2]
    b = 3
    while b <= num:
        for a in range(3, b, 2):
            if b % a == 0:
                b += 2
                #print('b1' + str(b))
                break
        else:
            primes.append(b)
            b += 2
            #print('b2' + str(b))
    return primes
num=int(input('please enter a number from 2 to nth: '))
a = is_prime(num)
print(a)