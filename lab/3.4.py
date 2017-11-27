# coding: utf-8
from sys import exit
Imie = ''
lista = open("imionabaza.txt", "r")
lista = lista.read()
lista2 = open('imionasuma.txt', 'a+')
lista2.seek(0)
lista2.write(lista)
while 1 > 0:
    Imie = raw_input("Wpisz imie").capitalize()
    if Imie == "Koniec":
        print lista2
        exit()
    elif Imie.isdigit():
        print "Uzywaj tylko liter"
    if lista.count(Imie) == 1:
        print "Lista zawiera juz to imie"
    else:
        lista2 = open('imionasuma.txt', 'a+')
        lista2.seek(0)
        lista2.write('\n')
        lista2.write(Imie)
        print lista2
        lista2.close()

