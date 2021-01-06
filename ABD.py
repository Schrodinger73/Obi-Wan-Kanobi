import math
import random
import matplotlib.pyplot as mpl
a = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 6, 6, 5]
f = input("Dice based(D) or Probability based(P) : ")
n = int(input("Balls : "))
array = []
array1 = []
array2 = []
for i in range(0, n):
    array1.append(a[random.randint(0, 26)])
for i in range(0, n):
    array2.append(random.randint(1, 6))
if f == "D":
    array = array2
    k = array2.count(5)
if f == "P":
    array = array1
    k = array1.count(5)


def sum_array(a):
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
    return sum


def cricket():
    if array.count(5) < 10:
        print("Final Score - " + str(sum_array(array) - 5 * array.count(5)) + " / " + str(k))
    if array.count(5) >= 10:
        cut_array(array, 5, 10)
        print("Final Score - " + str(sum_array(cut_array(array, 5, 10)) - 50) + " / 10")
    print(array)


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

array1 = array.copy()
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

array1 = ar(array1, 5, 10)


balls = [0]
for i in range(1, len(array1) + 1):
    balls.append(i)
runs = [0]
sum = 0
for i in range(0, len(array1)):
    sum += ar(array, 5, 10)[i]
    runs.append(sum)

(cricket())

mpl.plot(balls, runs)
mpl.xlabel("Balls")
mpl.ylabel("Runs")
mpl.show()
