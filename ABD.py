import random
import math
import time
import timeit

def is_prime(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    else:
            return True

def prime(a, b):
    array = []
    for i in range(a, b):
        if is_prime(i):
            array.append(i)
    return array

def sum_array(a):
    sum = 0
    for i in range(0, len(a)):
        sum = sum + int(a[i])
    return sum




def monty_hall(k):
    array = []
    for i in range(0, k):
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        if a == b:
            array.append(0)
        if a != b:
            array.append(1)
    return sum_array(array) / float(len(array))

a = [25, 77, 74, 50, 4, 57]
b = [25, 77, 74]

def delete(a, b):
    array = []
    for i in range(0, len(a)):
        if i != b:
            array.append(a[i])
    return array

def max(a):
    max = a[0]
    for i in range(0, len(a)):
        if a[i] > max:
            max = a[i]
    return max

def min(a):
    minimum = a[0]
    for i in range(0, len(a)):
        if a[i] < minimum:
            minimum = a[i]
    return minimum

def index_min(a):
    for i in range(0, len(a)):
        if a[i] == min(a):
            return i

def ascend(a):
    f = [min(a)]
    array = a
    for i in range(0, len(a) - 2):
        array = delete(array, index_min(array))
        f.append(min(array))

    f.append(max(a))
    return f

def reverse(a):
    array = []
    for i in range(0, len(a)):
        array.append(a[len(a) - i - 1])
    return array

def descend(a):
    return reverse(ascend(a))


r = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]




def blackjack(r):
    f = raw_input("Hit or Pass? : ")
    d = r
    l = []
    if f == "Hit":
        k = random.randint(0, len(d))
        array = delete(d, k)
        l.append(d[k])
        return l
    if f == "Pass":
        return sum_array(l)
    if sum_array(l) > 21:
        return "You lose."
    if sum_array(l) == 21:
        return "You won."
    return balck()

def balck():
    return blackjack(r)

def avg(a):
    return sum_array(a)/float(len(a))

def digits(a):
    array = []
    for i in range(0, len(str(a))):
        array.append(int(str(a)[i]))
    return array

def sum_digits(a):
    return sum_array(digits(a))

def sum_two_square(a):
    array = []
    for i in range(1, int(math.sqrt(int(a))) + 2):
        for j in range(1, int(math.sqrt(int(a))) + 2):
            if i < j:
                if i ** 2 + j ** 2 == a:
                    array.append([i, j])
    return array

def int_str(a):
    s = ""
    n = a
    while n > 0:
        s = s + str(n%10)
        n = n/10
    return s


rab = int(input("Kitne rabbits the ? "))
fox = int(input("Kitne fox the ? "))

def rabbit_fox(r, f):
    r = rab
    f = fox
    arrayr = [r]
    arrayf = [f]
    array = [[r, f]]
    while r > f:
        r = r - f
        f = 2 * f
        arrayr.append(r)
        arrayf.append(f)
        array.append([r, f])
    while r < f:
        u = random.randint(1, f - 1)
        r = int(3 * r / 2)
        f = f - u
        arrayr.append(r)
        arrayf.append(f)
        array.append([r, f])
    while f == r:
        arrayf.append(f)
        arrayr.append(r)
        array.append([r, f])
        break
    return "Rabbits - " + str(arrayr) + "    " + "Foxes - " +  str(arrayf) + "    " + "[Rabbit, Fox] - " + str(array) + "    " + "Ratio of rabbits = " + str(rab/float(r)) + "    Ratio of foxes = " + str(fox/float(f)) + "    Initial = " + str(rab/float(fox)) + "    Final = " + str(r/float(f))


#c = raw_input("Choose(Rabbit, Fox, r-f, Rab-r ratio, Fox-f ratio, Initial rab-fox ratio, Final r-f ratio) : ")

def conditional(rab, fox, c):
    r = rab
    f = fox
    arrayr = [r]
    arrayf = [f]
    array = [[r, f]]
    while r > f:
        r = r - f
        f = 2 * f
        arrayr.append(r)
        arrayf.append(f)
        array.append([r, f])
    while r < f:
        u = random.randint(1, f - 1)
        r = int(3 * r / 2)
        f = f - u
        arrayr.append(r)
        arrayf.append(f)
        array.append([r, f])
    while f == r:
        arrayf.append(f)
        arrayr.append(r)
        array.append([r, f])
        break
    if c == "Rabbit":
        return arrayr
    if c == "Fox":
        return arrayf
    if c == "r-f":
        return array
    if c == "Rab-r ratio":
        return rab/float(r)
    if c == "Fox-f ratio":
        return fox/float(f)
    if c == "Rab-r ratio, Fox-f ratio":
        return "Rabbit : " + str(rab/float(r)) + " Fox : " + str(fox/float(f))
    if c == "Initial rab-fox ratio":
        return rab/float(fox)
    if c == "Final r-f ratio":
        return r/float(f)
    if c == "Initial rab-fox ratio, Final r-f ratio":
        return "Initial : " + str(rab/float(fox)) + " Final : " + str(r/float(f))

def rab_more_fox(n):
    array = []
    for i in range(0, n):
        d = random.randint(5, 10000)
        g = random.randint(4, d)
        array.append(conditional(d, g, "Final r-f ratio"))
    return standard_deviation(array) + "    " + str(avg(array))
#    return str(array) + "      " + str(avg(array)) + " Hoot Hoot  " + standard_deviation(array)

start = time.time()

def standard_deviation(a):
    array = []
    for i in range(0, len(a)):
        array.append((avg(a) - a[i])**2)
    return str(math.sqrt(avg(array))) + "     " + str(math.sqrt(avg(array)) * 100 / float(avg(array))) + " %"


print(rab_more_fox(2000))

end = time.time()

print("Time : " + str(end - start))