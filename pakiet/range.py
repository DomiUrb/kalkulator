# funkcja do geenrowani liczb wg zadanych parametrow

liczby = range(5)
# print(type(liczby))
print(liczby)

# for
# for i in liczby: print(i) # będzie działać, ale to nie jest preferowane

# for i in liczby: #stop
#     print(i)

# for i in range(1,10): #start, stop
#     print(i)

# for i in range(1, 10, 2):  # start, stop, step (co 2)
#     print(i)

# for i in range(-10,10): #start, stop
#     print(i)

# for i in range(-10, 10, 2):  # start, stop, step (co 2)
#     print(i)

# for i in range(10, 1, -2):  # start, stop, step (co 2)
#     print(i)

# tekst = 'Kurs programowania w języku Python dla nieprogramistów'
# licznik = 0
#
# for i in tekst:
#     if i == 'P' or i == 'p':
#         licznik += 1  # skrócony zapis <=>licznik = licznik + 1
# print('Litera p wystapila: ', licznik, 'razy.')
#
# liczba1 = 1
# liczba2 = 1
#
# if liczba1 >= liczba2:
#     print('Pierwsza liczba większa lub rowna')
# else:
#     print('Druga liczba większa')

# liczba = int(input('Podaj liczbę: '))

# if liczba < 10:
#     print('Jest to mała liczba')
# elif 10 <= liczba < 100:
#     print('To juz większa liczba, ale mneijsza od 100')
# else: # else nie musi byc
#     print('To jest liczba powyzej 100')


# liczba = int(input('Podaj liczbę: '))
#
# if liczba < 10 or liczba > 15:
#     print('Liczba nie jest z odpowiedniego przedziału')


# liczba = int(input('Podaj liczbę: '))
# cyfry = [1, 3, 5, 7, 9]
#
# if liczba not in cyfry:
#     print('Liczby nie ma w zbiorze')
# else:
#     print('Liczba jest w zbiorze')


# nic = None  # odpowiednik NULL
# pusty_string = ''
#
# if not nic: # zawsze spelniony # if not - zaprzeczenie
#     print('None to null i False')
#
# if not pusty_string:
#     print('Pusty string to false')
#
# if nic == pusty_string:
#     print('none i pusty string to false')
#
# if pusty_string == '':
#     print('To jest pusty string')
#
# print(type(pusty_string))

#mozna zagniezdzac
# a = 1
# b = 3
#
# if a == 1:
#     print('jestem w a')
#     if b == 2:
#         print('jestem w B')
#     else:
#         print('to jest inna cyfra niz 2')
# else:
#     print('to jest inna cyfra nzi 1')

slownik = {'imie': 'Marek', 'nazwisko': 'Kowalski', 'plec': 'Mezczyzna'}

for key in slownik:
    print(key)

for val in slownik.values():
    print(val)

for key,values in slownik.items():
    print(key + '->',values)