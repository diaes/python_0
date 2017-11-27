# coding: utf-8
from sys import exit

set = raw_input("Liczba setek")
if set == "0":
    print "Liczba setek nie moze byc zero!".upper()
    exit(0)
dzie = raw_input("Liczba dziesiątek")
jed = raw_input("Liczba jednośći")

liczba = set + dzie + jed
print "Twoja liczba to %s" %liczba
kwadrat = int(liczba) ** 2
print "Kwadrat tej liczby to %s" %kwadrat


