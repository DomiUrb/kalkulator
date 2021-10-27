# Napisz program, który wyświetla dziewięć wierszy składających się z litery
# "0", z których każdy jest coraz dłuższy, i dziewięć takich samych wierszy,
# z których każdy jest coraz krótszy.
def rysunek(): # dajemy 3 apostrofy, enter meidzy nimi i docstring - opis slowny
    '''
    Funkcja, która rysuje strzałkę w prawo
    :return: print
    '''
    for i in range(10):
        print('O' * i)
    for i in range(10, 0, -1):
        print('O' * i)


# funkcja

# def strzalka():
#     pass  # usypia funkje, tak jakby byla skomentowana

def strzalka(n=4): # nie jest potrzebny return jak mamy printa(?) # n= 4 - przypisujemy domyslna wartosc 4, ktora program podstawi jak nie podamy innego argumentu
    for j in range(n):
        print(2 * " " + n * "0")
    for i in range(n//2+3):
        print(i * " " + (n+4-2*i) * "0")

#wywolanie funkcji
# strzalka(5)
# rysunek()

#print('MENU:')

# print('Podaj menu, masz do wyboru "strzalka" i "rysunek" :) : ')
# wejscie = input()
#
# def menu(f):
#     if f == 'strzalka':
#         strzalka()
#     elif f == 'rysunek':
#         rysunek()
#     else:
#         print('Nie ma tego w menu')
# menu(wejscie)


# while True:
#     x = input("""Wybierz jedno z poniższego MENU:
#     Strzałka w dół
#     Rysunek
#     """)
#     y = int(input("Podaj rozmiar elementu: "))
#
#     if x == "Strzałka w dół":
#         strzalka(y)
#     elif x == "Rysunek":
#         rysunek()
#     elif x == 'stop':
#         break
#     else:
#         print("Przepraszamy. Nie ma tego w menu.")
