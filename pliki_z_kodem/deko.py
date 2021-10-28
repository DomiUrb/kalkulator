import time


def wykonaj(funkcja, a, b):
    x = funkcja(a, b)
    return x


def dodaj(a, b):
    return a + b


# print(wykonaj(dodaj, 2, 3))


def glowna():
    def wewn(a, b):
        return a * b

    x = wewn(2, 4)
    return x


# print(glowna())


def funk():
    def funkW(a, b):
        return a * b

    return funkW


# x = funk()
# print(x(3,3))

# def zwyklaFunkcja():
#     print('To jest zwykla funkcja')
#
#
# def dekor(funkcja):
#     def wew():
#         print('Dekorujemy funkcje')
#         return funkcja()
#     return wew()
#
# test = dekor(zwyklaFunkcja)
# #print(test)


# def dekor(funkcja):  # dekory zawsze robimy na poczatku pliku, na samej gorze
#     def wew(*args, **kwargs):
#         print('Dekorujemy funkcje')
#         return funkcja(*args, **kwargs)
#
#     return wew
#
#
# @dekor
# def zwyklaFunkcja(a, b, c):
#     print('To jest zwykla funkcja')
#     print('Wynik: ', a + b + c)


#zwyklaFunkcja(1, 2, 3)

# tu import time trzeba, ale on sie sam robi

def dekor(funkcja):  # dekory zawsze robimy na poczatku pliku, na samej gorze
    def wew(*args, **kwargs):
        start = time.time()
        x = funkcja(*args, **kwargs)
        koniec = time.time()
        print(funkcja.__name__, 'wykonywala sie', koniec-start, 'sek')
        return x

    return wew


@dekor
def dodaj (a,b):
    time.sleep(1)
    return a+b

@dekor
def odejmij (a,b,c):
    time.sleep(0.5)
    return a-b-c

print(dodaj(2,2))
print(odejmij(1,2,3))


