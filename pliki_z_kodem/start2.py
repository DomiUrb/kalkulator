# Napisz program, który umieszcza na liście o nazwie lista 100 pseudolosowych
# liczb z przedziału od 1 do 100, a następnie sprawdza, czy wprowadzona
# z klawiatury liczba znajduje się na tej liście.

"""
wyświetlenie listy z wylosowanymi liczbami
input z podaną liczbą
print z informacją czy liczba podana w input jest w liście
"""


import random

lista = []
for i in range(1, 100):
    lista.append(random.randint(1, 100)) # lista = [random.randint (0,100) for _ in range(n)
print('Lista: ', sorted(lista))

while True:
    liczba = input (
'''
Podaj szukaną liczbę. Jeśli chcesz zatrzymać program - wpisz stop:
''')

    if str(liczba) == 'stop':
        break
    elif int(liczba) in lista:
        print('Liczba znajduje się na liście')
    elif int(liczba) not in lista:
        print('Liczby nie ma na liście')
    else:
        print('To nie jest liczba, spróbuj jeszcze raz :)')


# lista = [for i in range(1,100) ]
# random
#
# kostkaK6 = random.randint(1, 6)
# print('Rzut kością: ', kostkaK6)
