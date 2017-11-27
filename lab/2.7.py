# coding: utf-8
from math import sqrt
def parametry(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print "Brak pierwiastków"
    elif delta == 0:
        pierwiastek = -b * (2 * a) ** -1
        print "Jedynym pierwiastkiem równianie jest %s " %pierwiastek
    elif delta > 0:
        pierwiastek1 = (-b + sqrt(delta)) * (2 * a) ** -1
        pierwiastek2 = (-b - sqrt(delta)) * (2 * a) ** -1
        print "Pierwszym pierwiastek równania jest %s " %pierwiastek1
        print "Drugim pierwiastkiem równania jest %s " %pierwiastek2

parametry(2 ,10 ,8)