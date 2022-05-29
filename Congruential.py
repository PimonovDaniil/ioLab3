# linear congruential method
# а именно мультипликативный конгруэнтый метод
# если юзать для криптографии, произойдёт взлом жопы

global seed
seed = 1  # default


def setSeed(s):
    global seed
    seed = s


def rand():
    a = 16807
    m = 2147483647
    global seed
    seed = seed * a % m
    return seed
