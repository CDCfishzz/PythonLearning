import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r = move(100, 100, 60, math.pi / 6)
print(r)


def quadratic(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        raise TypeError("delta < 0, 此方程无实根")
    elif delta == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2


print("quadratic(2, 3, 1) = ", quadratic(2, 3, 1))
print("quadratic(1, -2, 1) = ", quadratic(1, 3, -4))

