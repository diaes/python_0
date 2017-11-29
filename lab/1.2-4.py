# coding: utf-8
tekst = "Litwo! Ojczyzno moja! ty jestes jak zdrowie."  \
        "Ile cię trzeba cenić, ten tylko się dowie," \
        "Kto cię stracił. Dziś piękność twą w całej ozdobie" \
        "Widzę i opisuję, bo tęsknię po tobie." \
        "Panno Święta, co Jasnej bronisz Częstochowy" \
        "I w Ostrej świecisz Bramie! Ty, co gród zamkowy" \
        "Nowogródzki ochraniasz z jego wiernym ludem!" \
        "Jak mnie dziecko do zdrowia powróciłaś cudem" \
        "(Gdy od płaczącej matki pod Twoję opiekę" \
        "Ofiarowany, martwą podniosłem powiekę" \
        "I zaraz mogłem pieszo do Twych świątyń progu" \
        "Iść za wrócone życie podziękować Bogu)," \
        "Tak nas powrócisz cudem na Ojczyzny łono." \
        "Tymczasem przenoś moję duszę utęsknioną" \
        "Do tych pagórków leśnych, do tych łąk zielonych," \
        "Szeroko nad błękitnym Niemnem rozciągnionych;" \
        "Do tych pól malowanych zbożem rozmaitem," \
        "Wyzłacanych pszenicą, posrebrzanych żytem;" \
        "Gdzie bursztynowy świerzop, gryka jak śnieg biała," \
        "Gdzie panieńskim rumieńcem dzięcielina pała," \
        "A wszystko przepasane, jakby wstęgą, miedzą" \
        "Zieloną, na niej z rzadka ciche grusze siedzą."
dlugosc = len(tekst)
samogloski = tekst.count('a') + tekst.count('e') + tekst.count('y') + tekst.count('i') + tekst.count('ą') /\
+ tekst.count('ę') + tekst.count('u') + tekst.count('ó')
spacje = tekst.count(' ')
inne = tekst.count(',') + tekst.count('!') + tekst.count('?') + tekst.count('.')
spolgloski = dlugosc - samogloski - spacje - inne

print "Tekst składa się z %s znaków w tym %s samogłosek ,%s spółglosek ,%s spacji i %s innych znaków." % \
      (dlugosc ,samogloski ,spolgloski ,spacje ,inne)
print tekst[::2]
print tekst[::3]
print tekst[::7]
wers = tekst[0:44]
print wers
print wers.replace("Litwo" ,"Polsko").upper()