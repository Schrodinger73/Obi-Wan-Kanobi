import math
import random

def guess():
    n1 = int(input("Lower Limit : "))
    n2 = int(input("Upper Limit : "))
    n = random.randint(n1, n2)
    ans = n2 + 20
    turns = 0
    while ans != n:
        ans = int(input("Guess : "))
        if ans < n:
            print("Too low!!!")
            turns += 1
            print("Count = " + str(turns))
        if ans > n:
            print("Too high!!!")
            turns += 1
            print("Count = " + str(turns))
        if ans == n:
            print("You got it!!!")
            turns += 1
            print("Your score is " + str(turns))
    print()

def factors(n):
    array = []
    for i in range(1, n + 1):
        if n % i == 0:
            array.append(i)
    return(array)

def is_prime(n):
    if len(factors(n)) == 2:
        return(True)
    else:
        return(False)

def sum_array(a):
    sum = 0
    for i in range(0, len(a)):
        sum += int(a[i])
    return(sum)

def is_perfect(n):
    if sum_array(factors(n)) == 2 * n:
        return(True)
    else:
        return(False)

def perfect_root(n, a):
    if math.pow(n, a) == int(math.pow(n, a)):
        return(True)
    else:
        return(False)

def divisible(n, a):
    if n % a == 0:
        return(True)
    else:
        return(False)

def is_cool_number(n):
    if is_perfect(n) or is_prime(n) or perfect_root(n, 0.5) or perfect_root(n, 1/float(3)) or divisible(n, 9) or divisible(n, 25) or divisible(n, 11) or divisible(n, 13) or n == 2004 or n == 2804 or n == 1977 or n == 1974:
        return(True)
    else:
        return(False)

def cool_numbers(a, b):
    array = []
    for i in range(a, b + 1):
        if is_cool_number(i):
            array.append(i)
    return(array)
        
    


        
