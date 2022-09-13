import math
import os 
import sys 
import subprocess
# print('  _____ _        _   _     _   _               \n /  ___| |      | | (_)   | | (_)              \n \ `--.| |_ __ _| |_ _ ___| |_ _  ___          \n  `--. | __/ _` | __| / __| __| |/ __|         \n /\__/ | || (_| | |_| \__ | |_| | (__          \n \____/ \__\__,_|\__|_|___/\__|_|\___|         \n            _            _       _             \n           | |          | |     | |            \n   ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ \n  / __/ _` | |/ __| | | | |/ _` | __/ _ \| ˙__|\n | (_| (_| | | (__| |_| | | (_| | || (_) | |   \n  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   \n🖩\n')
datagiven = []
adatokszama = 0
adatosszeg = 0
modos = {}
while True:
    adatokszama += 1
    adat1 = input(f'Tárolandó adat {adatokszama}: ')
    if adat1 == 'stop':
        adatokszama -=1
        break            
    try:
        adatosszeg = float(adatosszeg) + float(adat1)
        datagiven.append(float(adat1))
    except:
        print('Csak szám adható meg adatnak')
        adatokszama -=1
        if adat1 == 'stop':
            adatokszama -=1
            break 
print(f'Az érvényes megadott adatok: {datagiven}')
try:
    atlaag = adatosszeg/adatokszama
except:
    pass
def atlag():
    try:
        print(f'Az átlag: {adatosszeg/adatokszama}')
    except:
        print('Nullával nem lehet osztani!')
def median():
    datagiven.sort()
    kindian = datagiven[int(adatokszama/2)-1]
    if (adatokszama-1) % 2 == 0:
        print(f'A medián: {kindian + 0.5}')
    else:
        print(f' A medián: {kindian}')
def terj():
    maxim = 0
    minim = math.inf
    datagiven.sort()
    for i in datagiven:
        if i >= maxim:
            maxim = i
    for j in datagiven:
        if i <= minim:
            minim = j
    print(f'A terjedelem: {maxim-minim}')
def szoras():
    try:
        preosszeg = 0
        datagiven.sort(reverse=True)
        for i in datagiven:
            preszoras = (i - atlaag) ** 2
            preosszeg = preosszeg + preszoras
        rootable = preosszeg/adatokszama
        print(f'A szórás: {round(math.sqrt(rootable), 3)}')
    except:
        print('Nullával nem lehet osztani!')
def modusz():
    gyakr = -1 * (math.inf)
    masikgyakr = -1 * (math.inf)
    moduszok = []
    for i in datagiven:
        if i in modos.keys():
            modos[i] += 1 
        else:
            modos[i] = 1
    for j in modos:
        if modos[j] > gyakr:
            gyakr = modos[j]
            moduszok.append(gyakr)
        elif modos[j] == gyakr:
            pass
        else:
            pass
    print(f'Az adatsor módusza(i): {[key for key in modos.keys()][1]}')
    print(f'Előfordul {gyakr}-szor/szer/ször')
def szumma():
    print(f'Az adatok összege: {adatosszeg}')
def elemszam():
    print(adatokszama)
def szerkeszt():
    print(f'Az ön adatai: {datagiven}')
    melyik = input('Írja be, hányadik elemet szeretné szerkeszteni: ')
print('Érvényes műveletek: *átlag*, *medián*, *terjedelem*, *szórás*, *módusz*, *szumma*, *elemszám*, *szerkeszt*, *töröl*, *semmi*')
muvelet = input('Az elvégzendő művelet: ')
while True:
    if muvelet == 'átlag':
        atlag()
        muvelet = input('Az elvégzendő művelet: ')
    elif muvelet == 'medián':
        median()
        muvelet = input('Az elvégzendő művelet: ')
    elif muvelet == 'terjedelem':
        terj()
        muvelet = input('Az elvégzendő művelet: ')
    elif muvelet == 'szórás':
        szoras()
        muvelet = input('Az elvégzendő művelet: ')
    elif muvelet == 'módusz':
        modusz()
        muvelet = input('Az elvégzendő művelet: ')
    elif muvelet == 'szumma':
        szumma()
        muvelet = input('Az elvégzendő művelet: ')
    elif muvelet == 'elemszám':
        elemszam()
        muvelet = input('Az elvégzendő művelet: ')
    elif muvelet == 'töröl':
        subprocess.call([sys.executable, os.path.realpath(__file__)] +sys.argv[1:])
    elif muvelet == 'semmi':
        print('Semmilyen művelet nem lesz elvégezve')
        break
    else:
        print('Érvénytelen művelet!')
        muvelet = input('Az elvégzendő művelet: ')
sys.exit
# # A simple dictionary
# x = {'X':"yes", 'Y':"no", 'Z':"ok"}

# # To print a specific key (for example key at index 1)
# print([key for key in x.keys()][1])

# # To print a specific value (for example value at index 1)
# print([value for value in x.values()][1])

# # To print a pair of a key with its value (for example pair at index 2)
# print(([key for key in x.keys()][2], [value for value in x.values()][2]))

# # To print a key and a different value (for example key at index 0 and value at index 1)
# print(([key for key in x.keys()][0], [value for value in x.values()][1]))

# # To print all keys and values concatenated together
# print(''.join(str(key) + '' + str(value) for key, value in x.items()))

# # To print all keys and values separated by commas
# print(', '.join(str(key) + ', ' + str(value) for key, value in x.items()))

# # To print all pairs of (key, value) one at a time
# for e in range(len(x)):
#     print(([key for key in x.keys()][e], [value for value in x.values()][e]))

# # To print all pairs (key, value) in a tuple
# print(tuple(([key for key in x.keys()][i], [value for value in x.values()][i]) for i in range(len(x))))