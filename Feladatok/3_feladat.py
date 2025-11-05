"""Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, és a képernyőre kiírja, 
melyik a nagyobb szám! Kezeld azt az esetet is, ha a két szám egyenlő!
"""

szam1 = int(input('Írj ide egy számot: '))
szam2 = int(input('Írj ide még egy számot: '))

def eldontes():
    if szam1 > szam2:
        valasz = ('Az első szám nagyobb.')

    elif szam1 == szam2:
        valasz = ('Egyenlőek')

    else:
        valasz = ('A második szám nagyobb.')
    print(valasz)

eldontes()