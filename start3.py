import pakiet.kalkulator
from pakiet import kalkulator
#from pliki_z_kodem import rzutowanie
#import pakiet
import pyfiglet
# if __name__ == "__main__":
#     pass

#main - funkcja uruchomieniowa, pod spodem ją definiujemy

if __name__ == "__main__": # zeby uruchomic tylko to, co jest w mainie a nie wszxystjkoe, co jest za zaimportowane
    #wykres.wykres2()
    #listy
    #print('Witaj w moim programie')
    #pakiet.witaj()

    baner = pyfiglet.figlet_format("K A L K U L A T O R")
    print(baner)

    #baner = pyfiglet.Figlet(font = 'larry3d')
    #print(baner.renderText("W i t a j"), 'red')

while True:
    d = input(
'''Wybierz działanie z poniższej listy:
    "+", "-", "*", "/", "**" (potęga)
Aby zakończyć - wpisz stop
''' )
    #x = int(input ('Podaj pierwszą liczbę: '))
    #y = int(input('Podaj drugą liczbę (w przypadku potęgowania - podaj potęgę): '))

    #print(f'Wybrane przez Ciebie liczby: {x,y}' )
    #print('Wybrane działanie: ', d)

    if d == '+':
        print('Wybrano dodawanie')
        x = int(input ('Podaj pierwszą liczbę: '))
        y = int(input('Podaj drugą liczbę: '))
        print(f'Wybrane przez Ciebie liczby: {x,y}')
        kalkulator.dod(x,y)
    elif d == '-':
        print('Wybrano odejmowanie')
        x = int(input ('Podaj pierwszą liczbę: '))
        y = int(input('Podaj drugą liczbę: '))
        print(f'Wybrane przez Ciebie liczby: {x,y}' )
        kalkulator.odejm(x,y)
    elif d == '*':
        print('Wybrano mnożenie')
        x = int(input('Podaj pierwszą liczbę: '))
        y = int(input('Podaj drugą liczbę: '))
        print(f'Wybrane przez Ciebie liczby: {x, y}')
        kalkulator.mnoz(x,y)
    elif d == '/':
        print('Wybrano dzielenie')
        x = int(input('Podaj pierwszą liczbę: '))
        y = int(input('Podaj drugą liczbę: '))
        print(f'Wybrane przez Ciebie liczby: {x, y}')
        kalkulator.dziel(x,y)
    elif d == '**':
        print('Wybrano potęgowanie')
        x = int(input('Podaj podstawę: '))
        y = int(input('Podaj wykładnik: '))
        print(f'Wybrane przez Ciebie liczby: {x, y}')
        kalkulator.potega(x,y)
    elif d == 'stop':
        print('Koniec programu')
        break

