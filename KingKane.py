import math
import matplotlib.pyplot as plt
import random
a = [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6]
f = input("Dice based(D) or Probability based(P) : ")
#P1 = input("Player1(Blue) : ")
#P2 = input("Player2(Orange) : ")
P1 = "1"
P2 = "2"
n = int(input("Balls : "))
array2 = []
array = []
array5 = []
array6 = []
array7 = []
array8 = []
for i in range(0, n):
    array5.append(a[random.randint(0, len(a) - 1)])
for i in range(0, n):
    array6.append(a[random.randint(0, len(a) - 1)])
for i in range(0, n):
    array7.append(random.randint(1, 6))
for i in range(0, n):
    array8.append(random.randint(1, 6))
if f == "D":
    array = array7
    array2 = array8
    k1 = array7.count(5)
    k2 = array8.count(5)
if f == "P":
    array = array5
    array2 = array6
    k1 = array5.count(5)
    k2 = array6.count(5)
def sum_array(a):
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
    return sum
S1 = []
def cricket1():
    if array.count(5) < 10:
        S1.append(sum_array(array) - 5 * array.count(5))
        print("Final Score of " + P1 + " - " + str(S1[0]) + " / " + str(k1))
    if array.count(5) >= 10:
        S1.append(sum_array(cut_array(array, 5, 10)) - 50)
        cut_array(array, 5, 10)
        print("Final Score of " + P1 +" - " + str(S1[0]) + " / 10")
S2 = []
def cricket2():
    if array2.count(5) < 10:
        S2.append(sum_array(array2) - 5 * array2.count(5))
        print("Final Score of " + P2 + " - " + str(S2[0]) + " / " + str(k2))
    if array2.count(5) >= 10:
        S2.append(sum_array(cut_array(array2, 5, 10)) - 50)
        cut_array(array2, 5, 10)
        print("Final Score of " + P2 + " - " + str(S2[0]) + " / 10")

def final():
    if S1[0] > S2[0]:
        print(P1 + " wins!!!")
    if S1[0] < S2[0]:
        print(P2 + " wins!!!")
    if S1[0] == S2[0]:
        print("It's a draw!!!")

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
array3 = []

for i in range(0, len((ar(array, 5, 10)))):
    array1.append(ar(array, 5, 10)[i])

for i in range(0, len((ar(array2, 5, 10)))):
    array3.append(ar(array2, 5, 10)[i])

balls1 = [0]
for i in range(1, len(array1) + 1):
    balls1.append(i)

balls2 = [0]
for i in range(1, len(array3) + 1):
    balls2.append(i)

runs1 = [0]
sum1 = 0
for i in range(0, len(array1)):
    sum1 += ar(array, 5, 10)[i]
    runs1.append(sum1)

sum2 = 0
runs2 = [0]

for i in range(0, len(array3)):
    sum2 += ar(array2, 5, 10)[i]
    runs2.append(sum2)
def cricket():
    cricket1()
    cricket2()
    final()
    plt.plot(balls1, runs1)
    plt.plot(balls2, runs2)
    plt.xlabel("Balls")
    plt.ylabel("Runs")
    plt.show()

cricket()
