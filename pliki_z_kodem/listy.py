# lista = []
# lista2 = [1, 2, 3]
# lista3 = ['Tomek', 5, 9.78, False]
#
# lista2.reverse()
# lista2.append(4)  # dodaje na koncu list
#
# print(lista2)
# print(lista3)
# lista3[0] = 'Tytus'
# # lista3[4] = 'Tytus' # nei da sie, out of range
# # lista3[4:] = 'Tytus'
# # lista3[4:] = 9 # nie zadziala
# lista3[4:] = [9]
# lista3.insert(0, 52)  # podajemy indeks najpierw, nei podmienia tylko wchodzi na miejsce i przesuwa elementy
# lista3.sort()  # nie posortuje, bo są różne typy danych
#
# print(lista3)
# print(lista3[0])

# print(type(lista))
# Napisz program, który z listy dni_tyg = ['poniedziałek', 'wtorek',
# 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela'] pobiera wycinek
# z elementów listy o indeksach od 2 do 6.

# dni_tyg = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
# print(dni_tyg[2:6])
# dni_tyg.pop() #usuwa elementy z listy (domyslnie ostatni)
# dni_tyg.pop(0)
# dni_tyg.clear()  # czysci liste

# pobieranie pierwszych liter dla kazdego dnia z listy
dni_tyg = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']

# moje
for i in dni_tyg:
    print(i[0])

# prowadzącego
for i in range(len(dni_tyg)):
    print(dni_tyg[i][0])
