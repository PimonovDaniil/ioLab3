import math
import random


def cube(x, y, z):
    size = 10
    # Если точка находится в кубе ()
    if (x <= size) and (y <= size) and (z <= size) and (x >= 0) and (y >= 0) and (z >= 0):
        return True
    else:
        return False


def cilindr(x, y, z):
    cubeSize = 10  # ДОЛЖЕН СОВПАДАТЬ С РАЗМЕРОМ КУБА
    radCilindr = 3
    hCilindr = 10
    rast = math.sqrt((x - (cubeSize / 2)) ** 2 + (y - (cubeSize / 2)) ** 2)
    if rast <= radCilindr and cubeSize <= z <= cubeSize + hCilindr:
        return True
    else:
        return False


def cilindrVkube(x, y, z):
    cubeSize = 10  # ДОЛЖЕН СОВПАДАТЬ С РАЗМЕРОМ КУБА
    radCilindr = 3
    hCilindr = 5
    rast = math.sqrt((x - (cubeSize / 2)) ** 2 + (y - (cubeSize / 2)) ** 2)
    if rast <= radCilindr and cubeSize <= z <= cubeSize + hCilindr:
        return True
    else:
        return False


def monteKarlik(cube, cilindr, vAnal):
    P = [20, 20, 20]
    print("Объём фигур аналитически: ", vAnal)
    print("Объём пространства в пределах которого генерируем случайные точки: ", P[0] * P[1] * P[2])

    pointIn = 0
    pointOut = 0
    for i in range(100000):
        x = random.random() * P[0]
        y = random.random() * P[1]
        z = random.random() * P[2]
        if cube(x, y, z) or cilindr(x, y, z):
            pointIn += 1
        else:
            pointOut += 1
    print("Кол-во точек попало в пределы фигур: ", pointIn)
    print("Кол-во точек не попало в пределы фигур: ", pointOut)
    print("Объём посчитанный методом монте-карла", ((P[0] * P[1] * P[2]) * pointIn) / (pointOut + pointIn))
    print("Разница между аналитическим и Монте-Карло", abs((((P[0] * P[1] * P[2]) * pointIn) / (pointOut + pointIn)) - vAnal))
    print("Величина относительной среднеквадратической погрешности оценок объема: ",
          math.sqrt(pointOut / ((pointIn + pointOut) * pointIn)))


print("Куб со стороной 10, цилинтр с радиусом 3 и высотой 10")
monteKarlik(cube, cilindr, (10 * 10 * 10) + (math.pi * 9 * 10))
print("\nКуб со стороной 10, цилинтр с радиусом 3 и высотой 10 но на половину в кубе")
monteKarlik(cube, cilindrVkube, (10 * 10 * 10) + (math.pi * 9 * 5))
