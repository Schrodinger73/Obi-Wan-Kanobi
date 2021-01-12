import math
import random
import dictionary

a = input("Word : ")
a = a.split(" ")
n = int(input("Guess Limit : "))
ar = []
for i in range(0, len(a) - a.count(" ")):
    ar.append("-")
print(ar)

def replace(a, g):
    array = []
    for i in range(0, len(a)):
        if a[i] == g:
            array.append(i)
    return array

def replaced(a1, a2, g): # a1 is a, and a2 is ***
    for i in range(0, len(replace(a1, g))):
        a2[replace(a1, g)[i]] = g
    return a2

def arr_to_str(a):
    str = ""
    for i in range(0, len(a)):
        str += a[i] + " "
    return str



count = 0
while count < n and ar != a:
    g = input("Guess : ")
    if g in a:
        ar = replaced(a, ar, g)
        print(ar)
        print("Guesses left : " + str(n - count))
    if g not in a:
        print(ar)
        count += 1
        print("Guesses left : " + str(n - count))
    if count == n and ar != a:
        print("The man is guilty!!!")
        print("Original Word : " + arr_to_str(a))
    if ar == a:
        print("You won with " + str(count) + " wrong guess/es")

