liczby2slowa = {1: 'Jeden', 2: 'Dwa', 3: 'Trzy', 4: 'Cztery', 5: 'Piec', \
             6: 'Szesc', 7: 'Siedem', 8: 'Osiem', 9: 'Dziewiec', 10: 'Dziesiec', \
            11: 'Jedenascie', 12: 'Dwanascie', 13: 'Trzynascie', 14: 'Czternascie', \
            15: 'Pietnascie', 16: 'Szesnascie', 17: 'Siedemnascie', 18: 'Osiemnascie', \
            19: 'Dziewietnascei', 20: 'Dwadziescia', 30: 'Trzydziscie', 40: 'Czterdziesci', \
            50: 'Piecdziesiat', 60: 'Szescdziesiat', 70: 'Siedemdziesiat', 80: 'Osiemdziesiat', \
            90: 'Dziewiezdziesait', 0: 'Zero'}

def l2s(n):
    try:
        print liczby2slowa[n]
    except KeyError:
        try:
            print liczby2slowa[n-n%10] + liczby2slowa[n%10].lower()
        except KeyError:
            print 'Number out of range'


