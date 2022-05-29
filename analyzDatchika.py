from Congruential import *
import matplotlib
import matplotlib.pyplot as plt
from sklearn import datasets
import seaborn as sns

iris = datasets.load_iris()
kol_vo_stolbcov = 10
randomNumbers = []
x = list(range(2147483647//kol_vo_stolbcov, 2147483647, 2147483647//kol_vo_stolbcov))
y = [0]*kol_vo_stolbcov

for i in range(100000):
    r = rand()
    randomNumbers.append(r)
    for j in range(len(x)):
        if r < x[j]:
            y[j] += 1
            break
mat_ozhid = 0
m_circumflex_2 = 0
for i in range(len(x)):
    mat_ozhid += (x[i] * (y[i]/sum(y)))
    m_circumflex_2 += ((x[i]**2) * (y[i] / sum(y)))
dispers = m_circumflex_2 - (mat_ozhid**2)

print("Мат ожидание: "+str(mat_ozhid))
print("Дисперсия: "+str(dispers))

sns.barplot(x=x, y=y)
matplotlib.pyplot.show()
