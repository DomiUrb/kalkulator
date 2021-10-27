# lambda - funkcja tymczasowa, bez nazwy, ad hoc, tylko tu i teraz, lambda jest funkcja wyzszego rzedu, najczesciej argumentem sa liczby, rzedziej listy (ale tez z liczbami)
#
# lambda <parametry> : <wyrażenie>
# najpierw zarys, argumenty (moze byc wiecej niz 2), wzor i na koncu wartosci tych argumentow, wazna jest kolejnosc taka jak przy definicji argumentow
# print((lambda x, y: x + y)(3, 4))
# print((lambda x, y: x + y)('tomek', 'domek'))
# print((lambda x, y: x* y)('tomek', 2))
#
# lambda _: _ + 1 # _ -> brak anzwy parametru, powieksza wynik o 1)
#
# print((lambda _: _ + 1)(5)) # -> wynikiem 6
#
# liczymy = lambda x, y: x * y
#
# print(liczymy(3, 5))  # nie zadziala jak damy liczymy(3,5) i potem print (liczymy), trzebe wszystko na raz,

from functools import reduce

lista = [1, 3, 5, 7]
print(f"Nasza lista: {lista}\n")
print(f"Zastosowanie map: {list(map(lambda _: _ * 2, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda _: _ > 3, lista))}")
print(f"Zastosowanie reduce: {reduce(lambda x, y: x + y, lista)}") #funkcja wbudowana dodaje wszystkie elementy z listy -> redukuje elementy z listy i tworzy jeden - sume wszystkich


