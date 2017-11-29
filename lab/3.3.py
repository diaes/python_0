# coding: utf-8
from sys import exit
lista = list()
Imie = ''
while 1 > 0:
    Imie = raw_input("Wpisz imie").capitalize()
    if Imie == "Koniec":
        print lista
        lista = '\n'.join(lista)
        f = open('imionabaza.txt', 'wt+')
        f.write(lista)
        exit()
    elif Imie.isdigit():
        print "Uzywaj tylko liter"
    if lista.count(Imie) == 1:
        print "Lista zawiera juz to imie"
    else:
        lista.append(Imie)
else:
    print lista


