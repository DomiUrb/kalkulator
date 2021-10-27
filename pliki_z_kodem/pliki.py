'''
modyfikatory dostepow w pythonie
w - zapis, nadpisanie!
r - odczyt
a - zapis z zachowaniem poprzednich tresci w pliku
'''

#uchwyt = open('plik.txt', 'r', encoding='utf-8')
# uchwyt2 = open(r'C:\Users\CSComarch\PycharmProjects\pythonProject\pliki_z_kodem\plik.txt') # sciezka bezwzgledna, najpierw literka r!

#uchwyt.write('Tutaj treść nr 1\nTutaj treść nr 2\nTutaj treść nr 3')

# uchwyt.write('''
# modyfikatory dostepow w pythonie
# w - zapis, nadpisanie!
# r - odczyt
# a - zapis z zachowaniem poprzednich tresci w pliku
# ''')

#uchwyt.write('\n\tA tutaj powinny byc inne info')

# dane = uchwyt.read()
# print(dane)

# while True:
#     dane = uchwyt.read(1024) #blokada bitów, zeby nie odczytywac za duzo danych
#     print(dane, end = '')
#     if not dane:
#         uchwyt.close()
#         break

try:
    with open('plik.txt', 'r', encoding='utf-8') as plik:
        for linia in plik:
            print(linia, end = '')
except IOError: #input/output error
    print('Brak pliku albo zla nazwa')