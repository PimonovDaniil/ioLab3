def cube(x, y, z):
    size = 10
    # Если точка находится в кубе ()
    if (x <= size) and (y <= size) and (z <= size) and (x >= 0) and (y >= 0) and (z >= 0):
        return True
    else:
        return False

