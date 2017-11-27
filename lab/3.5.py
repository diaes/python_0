# coding: utf-8
from sys import exit
lista = list()
Imie = ''
while True:
    Imie = raw_input("Wpisz imie").capitalize()
    if Imie == "Koniec":
        listaxy = open('imionaXY.txt', 'r')
        listaxy.seek(0)
        lines = sorted(listaxy.readlines())
        print "Imiona męskie: %s" %lines
        listaxy.close()
        listaxx = open('imionaXX.txt', 'r')
        listaxx.seek(0)
        lines = sorted(listaxx.readlines())
        print "Imiona damskie: %s" %lines
        listaxx.close()
        exit()
    elif Imie.isdigit():
        print "Uzywaj tylko liter"
    if lista.count(Imie) == 1:
        print "Lista zawiera juz to imie"
    else:
        if (Imie[-1] == 'a') and (Imie != "Jarema") and (Imie != "Kuba") and (Imie != "Bonawentura") and (Imie != "Barnaba") and (Imie != "Kosma"):
          lista2 = open('imionaXX.txt', 'a+')
          lista2.seek(0)
          lista2.write(Imie)
          lista2.write('\n')
          print lista2
          lista2.close()
        else:
            lista2 = open('imionaXY.txt', 'a+')
            lista2.seek(0)
            lista2.write(Imie)
            lista2.write('\n')
            print lista2
            lista2.close()
