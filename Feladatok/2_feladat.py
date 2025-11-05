"""Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja,
hogy negatív, pozitív vagy nulla-e! """

szam = int(input('Írj ide egy számot: '))

def eldontes(num):
    valasz = ()
    if num > 0:
        valasz = ('pozitív')

    elif num == 0:
        valasz = ('nulla')

    else:
        valasz = ('negatív')
    print(f'Ez a szám: {valasz}')

eldontes(szam)