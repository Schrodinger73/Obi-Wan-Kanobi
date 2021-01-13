import math
import random
import dictionary


ar1 = []
f = open("/Users/viralchitlangia/Documents/word.txt", "r")
for x in f:
    if len(x) >= 7:
        x1 = ""
        for i in range(0, len(x) - 1):
            x1 += x[i]
        ar1.append(x1)

a = ar1[random.randint(0, len(ar1) - 1)]
n = 7

ar = []
for i in range(0, len(a) - a.count(" ")):
    ar.append(" _ ")


def arr_to_str(a):
    str = ""
    for i in range(0, len(a)):
        str += a[i]
    return str

print(arr_to_str(ar))

def str_array(s):
    ar = []
    for i in range(0, len(s)):
        ar.append(s[i])
    return ar

a = str_array(a)

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
        str += a[i]
    return str


ar2 = []
count = 0
while count < n and ar != a:
    g = input("Guess : ")
    if g in ar2:
        print("Already guessed. Try again.")
        print("Guesses left : " + str(n - count))
        print(arr_to_str(ar))
    if g == arr_to_str(a):
        ar = a
        print("You won with " + str(count) + " wrong guess/es")
        break
    if g in a and g not in ar2:
        ar = replaced(a, ar, g)
        print(arr_to_str(ar))
        print("Guesses left : " + str(n - count))
        ar2.append(g)
    if g not in a and g not in ar2:
        print(arr_to_str(ar))
        count += 1
        print("Guesses left : " + str(n - count))
        ar2.append(g)
    if count == n and ar != a:
        print("The man is guilty!!!")
        print("Original Word : " + arr_to_str(a))
        break
    if ar == a:
        print("You won with " + str(count) + " wrong guess/es")
        break

