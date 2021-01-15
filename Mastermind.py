import random
import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
max_count = int(input("Count : "))
ar1 = []
for j in range(0, 4):
    ar1.append(numbers[random.randint(0, 7)])

def str_int_array(a):
    ar = []
    for i in range(0, len(a)):
        ar.append(int(a[i]))
    return ar

array = str_int_array(input("Guess : ").split(", "))




count = 1
red = 0
white = 0
while array != ar1:
    if count < max_count:
        red = 0
        white = 0
        for i in range(0, 4):
            if array[i] in ar1 and array[i] == ar1[i]:
                red += 1
            if array[i] in ar1 and array[i] != ar1[i]:
                white += 1

        print(str(red) + " Reds and " + str(white) + " Whites")
        count += 1
        print(str(max_count - count + 1) + str(" turns left"))
        array = str_int_array(input("Guess : ").split(", "))
    if count == max_count:
        print("Oops! Your turns are up!!!")
        print("Correct sequence - " + str(ar1))
        break
if array == ar1:
    print("You got it!!!")
    print("Turns taken - " + str(count))



