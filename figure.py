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
    print("Объём фигур аналитически: ", vAnal)
    print("Объём пространства в пределах которого генерируем случайные точки: ", 20 * 20 * 20)

    pointIn = 0
    pointOut = 0
    for i in range(100000):
        x = random.random() * 20
        y = random.random() * 20
        z = random.random() * 20
        if cube(x, y, z) or cilindr(x, y, z):
            pointIn += 1
        else:
            pointOut += 1
    print("Кол-во точек попало в пределы фигур: ", pointIn)
    print("Кол-во точек не попало в пределы фигур: ", pointOut)
    print("Объём посчитанный методом монте-карла", ((20 * 20 * 20) * pointIn) / (pointOut + pointIn))
    print("Разница между аналитическим и Монте-Карло", abs((((20 * 20 * 20) * pointIn) / (pointOut + pointIn)) - vAnal))


print("Куб со стороной 10, цилинтр с радиусом 3 и высотой 10")
monteKarlik(cube, cilindr, (10 * 10 * 10) + (math.pi * 9 * 10))
print("\nКуб со стороной 10, цилинтр с радиусом 3 и высотой 10 но на половину в кубе")
monteKarlik(cube, cilindrVkube, (10 * 10 * 10) + (math.pi * 9 * 5))
