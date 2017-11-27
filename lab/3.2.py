# coding: utf-8
lista = list()
x = 0
while (x < 10):
    Imie = raw_input("Wpisz imie")
    Imie = Imie[0].upper() + Imie[1::1]
    if Imie.isdigit():
        print "Uzywaj tylko liter"
    else :
        if (lista.count(Imie) == 1):
            print "Lista zawiera juz to imie"
        else:
            lista.append(Imie)
            x = x + 1

else :
    print lista