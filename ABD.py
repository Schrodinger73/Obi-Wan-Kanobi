import math
import random
import matplotlib.pyplot as mpl
a = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 6, 6, 5]
n = int(input("Balls : "))
array = []
for i in range(0, n):
    array.append(a[random.randint(0, 26)])

def sum_array(a):
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
    return sum


def cricket():
    if array.count(5) < 10:
        return "Final Score - " + str(sum_array(array) - 5 * array.count(5)) + " / " + str(array.count(5))
    if array.count(5) >= 10:
        cut_array(array, 5, 10)
        return "Final Score - " + str(sum_array(cut_array(array, 5, 10)) - 50) + " / 10"


def cut_array(a, j, n): #(array, element, number)
    count = 0
    cut = []
    i = 0
    while count < n and i < len(a):
        if a[i] != j:
            cut.append(a[i])
            i += 1
        if a[i] == j:
            cut.append(a[i])
            count += 1
            i += 1
    if count >= n or i >= len(a):
        return cut


def ar(a, n, k):
    ar = []
    if a.count(n) < k:
        ar = a
        for i in range(0, len(a)):
            if a[i] == n:
                ar[i] = 0
    if a.count(n) >= k:
        ar = cut_array(a, n, k)
        for i in range(0, len(cut_array(a, n, k))):
            if ar[i] == n:
                ar[i] = 0
    return ar

array1 = []

for i in range(0, len((ar(array, 5, 10)))):
    array1.append(ar(array, 5, 10)[i])

balls = [0]
for i in range(1, len(array1) + 1):
    balls.append(i)
runs = [0]
sum = 0
for i in range(0, len(array1)):
    sum += ar(array, 5, 10)[i]
    runs.append(sum)

print(cricket())

mpl.plot(balls, runs)
mpl.xlabel("Balls")
mpl.ylabel("Runs")
mpl.show()
