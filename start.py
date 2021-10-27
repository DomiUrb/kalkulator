#from pakiet import *
# from pakiet import * # daje dostep do wszystkich plikow wpisanych na na liscie w __init__.py, * -> wszystko, * dzialala, to musi byc wszystko wymeinione w tym plik __all__
# jak plik __a__ jest pusty, to tez zadziala, tylko trzeba wymieniac te nazwy plikow jak nizej
# from pakiet import wykres # mozna wpisywac pliki po przecinku, ale nie powinno sie w jednej linijce robic
# from pakiet import wykres, strzalka
# from pakiet import wykres as w # mozna dawać aliasy i wtedy wywolujemy w.wykres itd
#strzalka.rysunek()

# pakiet.strzalka.rysunek()
# pakiet.strzalka.strzalka(6)

# import pakiet.range

# wykres.wykres()
# strzalka.strzalka(5)
# wykres.wykres2()

# from pliki_z_kodem import rzutowanie

# rzutowanie

# printow sie nie returnuje, albo jest print albo return
# def powiel(tekst, ile):
#     print ((tekst + ' ') * ile)

# powiel('fff', 5)
# print(powiel('fff', 5))

# tablica = [powiel('tt', 5), False]
# print(tablica)


# def powiel(tekst = 'Nie podałeś wartości', ile=1): # jak jest kilka argumentow i jeden ma byc domyslny, to wszystkie juz musza miec zdefiniwoana domyslna wartosc
#     print ((tekst + ' ') * ile)
#
#
# #powiel('2',3)
# powiel(ile = 5) # wtedy wezmie tekst domyslny

# argumenty zmienne

def duzo(*args, **kwargs): #gwiazdki - * nieograniczona liczba nienazwanych argumentow, ** nieograniczona liczba argumentow nazwanych (z kluczem)
    print(args)
    print(kwargs)
#
# duzo(3,43,5.7,'Tomek',wiek=38)
# duzo()


# def duzo(imie, *args, **kwargs):  # tak nie robimy, jak juz kwargs i args to nie inne
#     print(args)
#     print(imie)
#     print(kwargs)


# duzo(3,43,5.7,'Tomek',wiek=38)
# duzo(True, 43, 222)

# duzo('Tomek', 3, 5, 6, wiek=5)
# duzo(True, 3, 5, 6)

a=5

def mam_global():
    global a # i a z tej funkcji staje sie globalne, stosujemy tylko jak nie ma innego wyjscia
    a = 1
    b = 2
    return a + b


def nie_mam_globala():
    c = 3
    return a + c


print(mam_global())
print(nie_mam_globala())
print(a)