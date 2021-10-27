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

d = input(
'''Wybierz działanie z poniższej listy:
+
-
*
/
** (potęga)
'''         )
x = int(input ('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę (w przypadku potęgowania - podaj potęgę: '))

print(f'Wybrane przez Ciebie liczby: {x,y}' )
print('Wybrane działanie: ', d)

if d == '+':
    kalkulator.dod(x,y)
elif d == '-':
    kalkulator.odejm(x,y)
elif d == '*':
    kalkulator.mnoz(x,y)
elif d == '/':
    kalkulator.dziel(x,y)
elif d == '**':
    kalkulator.potega(x,y)

