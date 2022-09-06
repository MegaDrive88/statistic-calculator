import math

print('  _____ _        _   _     _   _               \n /  ___| |      | | (_)   | | (_)              \n \ `--.| |_ __ _| |_ _ ___| |_ _  ___          \n  `--. | __/ _` | __| / __| __| |/ __|         \n /\__/ | || (_| | |_| \__ | |_| | (__          \n \____/ \__\__,_|\__|_|___/\__|_|\___|         \n            _            _       _             \n           | |          | |     | |            \n   ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ \n  / __/ _` | |/ __| | | | |/ _` | __/ _ \| ˙__|\n | (_| (_| | | (__| |_| | | (_| | || (_) | |   \n  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   \n')
datagiven = []
adatokszama = 0
adatosszeg = 0
while True:
    adatokszama += 1
    adat1 = input(f'Tárolandó adat {adatokszama}: ')
    if adat1 == 'stop':
        break            
    try:
        adatosszeg = float(adatosszeg) + float(adat1)
        datagiven.append(float(adat1))
    except:
        print('Csak szám adható meg adatnak')
        adatokszama -=1
        if adat1 == 'stop':
            break 
print(f'Az érvényes megadott adatok: {datagiven}')

def atlag():
    print(f'Az átlag: {adatosszeg/adatokszama}')

print('Érvényes műveletek:...')
muvelet = input('Az elvégzendő művelet: ')

if muvelet == 'átlag':
    atlag()
# adatok szerkesztése is kéne, mint művelet                                  