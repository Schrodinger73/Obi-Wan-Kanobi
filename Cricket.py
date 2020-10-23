import math
import random

# Sum of all values in an array
def sum_array(a):
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
    return sum

# Returns output of a random dice roll
def dice():
    return random.randint(1, 6)

# Returns score after 'n' balls, where '5' is "Out", and other values on the dice correspond to runs.
def cricket(n):
    array = []
    i = 1
    while i <= n and array.count(5) < 10:
        array.append(dice())
        i += 1
    return str(sum_array(array) - 5 * array.count(5)) + "/" + str(array.count(5)) + " in " + str(len(array)) + " balls."
        
    
