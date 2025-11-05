"""Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja,
és egy eljárás segítségével meghatározza,
és a képernyőre kiírja, melyik a legrövidebb szó! """

szo1 = input('Mondj egy szót ')
szo2 = input('Mondj egy második szót ')
szo3 = input('Mondj egy harmadik szót ')

szavak_listaja =[szo1 , szo2 , szo3]

# 1. megoldás
# def eldontes():
#     if len(szo1) < len(szo2) and len(szo1 ) < len(szo3):
#         print(f'A legkisebb szó: {szo1}')
    
#     elif len(szo2) < len(szo1) and len(szo2) < len(szo3):
#         print(f'A legkisebb szó: {szo2}')

#     elif len(szo3) < len(szo1) and len(szo3) < len(szo2):
#         print(f'A legkisebb szó: {szo3}')

#     else:
#         print('A szavak ugyanakkorák vagy nincs legkisebb szó.')

# 2. medolás
# def eldontes(szavak):
#     legrovidebb = min(szavak,key=len)
#     print(f'A legrövidebb szó: {legrovidebb}')


# 3. megoldás

def eldontes(szavak):
    legrovidebb =len(szavak[0])
    legrovidebb_szo = szavak[0]
    for szo in szavak:
        if len(szo) < legrovidebb:
            legrovidebb = len(szo)
            legrovidebb_szo = szo
    print(f'A legrövidebb szó: {legrovidebb_szo}')


eldontes(szavak_listaja)
