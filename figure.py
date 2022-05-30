import math


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
    rast = math.sqrt((x - (cubeSize / 2)) ** 2 + (y - (cubeSize / 2)) ** 2 + (z - (cubeSize / 2)) ** 2)
    if rast <= radCilindr and cubeSize <= x <= cubeSize + hCilindr:
        return True
    else:
        return False
