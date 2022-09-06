import math

print('  _____ _        _   _     _   _               \n /  ___| |      | | (_)   | | (_)              \n \ `--.| |_ __ _| |_ _ ___| |_ _  ___          \n  `--. | __/ _` | __| / __| __| |/ __|         \n /\__/ | || (_| | |_| \__ | |_| | (__          \n \____/ \__\__,_|\__|_|___/\__|_|\___|         \n            _            _       _             \n           | |          | |     | |            \n   ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ \n  / __/ _` | |/ __| | | | |/ _` | __/ _ \| ˙__|\n | (_| (_| | | (__| |_| | | (_| | || (_) | |   \n  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   \n')
datagiven = []
adatokszama = 0
while True:
    adatokszama += 1
    adat1 = input(f'Tárolandó adat {adatokszama}: ')
    datagiven.append(adat1)
    if adat1 == 'stop':
        datagiven.remove('stop')
        break
print(f'A megadott adatok: {datagiven}')

muvelet = input('Az elvégzendő művelet: ')
                                              
# adatok szerkesztése is kéne, mint művelet                                  