import math
import random

def sum_array(a):
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
    return sum

def dice():
    return random.randint(1, 6)

def cricket(n):
    array = []
    i = 1
    while i <= n and array.count(5) < 10:
        array.append(dice())
        i += 1
    return array, sum_array(array) - 5 * array.count(5)
        
    
