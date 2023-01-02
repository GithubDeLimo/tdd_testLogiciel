from math import pi, degrees
from math import acos


def max_int(a, b):
    if a < b:
        return b
    else:
        return a


def min_int(list):
    min = list[0]
    for i in range(len(list)):
        if list[i] <= min:
            min =list[i]
    return min


def mysqrt(a):
    return round(a**0.5, 2)


def perimeter(r):
    #pi = 3.14;
    return round(2*pi*r, 2)


def angle(a, b, c):
    if (((a + b) > c) & ((a + c) > b) & ((b + c) > a)) == 0:
        return False
    else:
        A = acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
        B = acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
        C = acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

        angleA = round(degrees(A))
        angleB = round(degrees(B))
        angleC = round(degrees(C))

        return angleA, angleB, angleC



