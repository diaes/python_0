# coding: utf-8
def XD(liczba):
    if liczba < 0:
        print "-1000"
    elif liczba == 0:
        print "ZEROOOO!!!!"
    elif liczba > 0 and liczba < 10:
        print liczba
    elif liczba >= 10 and liczba <= 100:
        print "dużo"
    elif liczba > 100:
        print "bardzo dużo"
pro = float(raw_input("Daj liczbe"))
while (pro.is_integer() == True):
    XD(pro)
    pro = float(raw_input("Daj liczbe"))
else:
    print "Działą tylko z liczbami całkowitymi"

