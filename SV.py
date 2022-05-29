import random
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import math


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


# https://habr.com/ru/post/265321/


def Bernoulli(p):
    boundary = (1 - p)
    if random.random() > boundary:
        return 1
    else:
        return 0


# СВ с биномиальным распределением
def BinomialBernoulli(p, n):
    sum = 0
    i = 0
    while i != n:
        i += 1
        sum += Bernoulli(p)
    return sum


# Сам полином
def Pn(m, p, n):
    c = math.factorial(n) / (math.factorial(m) * math.factorial(n - m))
    return c * (p ** m) * ((1 - p) ** (n - m))


polinom = []
for i in range(15):
    polinom.append(Pn(i, 0.35, 15))

res = [0] * 15
y = list(range(15))

for i in range(100000):
    r = BinomialBernoulli(0.35, 15)
    try:
        res[r] += 1
    except:
        pass

# приводим к диапазону [0, 1]
s = sum(res)
for i in range(len(res)):
    res[i] /= s
sns.barplot(x=y, y=res, color='red')
# sns.barplot(x=y, y=polinom, color='blue')
plt.plot(y, polinom)
matplotlib.pyplot.show()
