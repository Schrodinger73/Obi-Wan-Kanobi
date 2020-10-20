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
