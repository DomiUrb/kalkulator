# enkapsulacja - hermetyzacja - sprobujemy ukryc niektore metody zeby byly na uzytek wlasny klasy
# dodajemy 2 podlogi przed nazwy argumentow - ukrywa szczegoly implementacji klasy, ni podejrzymy printem

# class Samochod:
#
#     def __init__(self):
#         self.__silnik = False
#         self.__bieg = 0
#         self.__predkosc = 0
#
#     def uruchom(self):
#         self.__silnik = True
#
#     def __wylacz(self):
#         self.__silnik = False
#
#     def biegWyzej(self):
#         if self.__bieg < 6: self.__bieg += 1; print(
#             self.__bieg)  # jednolinijkowa konstrukcja ifa, jak mamy tylko warunek + else
#
#     def biegNizej(self):
#         if self.__bieg >= 0: self.__bieg -= 1; print(
#             self.__bieg)  # jednolinijkowa konstrukcja ifa, jak mamy tylko warunek + else
#
#     def przyspiesz(self):
#         if self.__silnik == True and self.__bieg > 0: self.__predkosc += 10; print(self.__predkosc)
#
#     def hamuj(self):
#         if self.__predkosc >= 10:
#             self.__predkosc -= 10
#         else:
#             self.__predkosc = 0
#         print(self.__predkosc)

#tesla - automat - przyklad uzycia hermetyzacji - automatyczna skrzynia biegow, uzytkownik sam nie moze go zmienic
class Samochod:

    def __init__(self):
        self.__silnik = False
        self.__bieg = 0
        self.__predkosc = 0

    def uruchom(self):
        self.__silnik = True

    def wylacz(self):
        self.__silnik = False

    def __biegWyzej(self):
        if self.__bieg < 6: self.__bieg += 1; print(
            self.__bieg)  # jednolinijkowa konstrukcja ifa, jak mamy tylko warunek + else

    def __biegNizej(self):
        if self.__bieg >= 0: self.__bieg -= 1; print(
            self.__bieg)  # jednolinijkowa konstrukcja ifa, jak mamy tylko warunek + else

    def przyspiesz(self):
        if self.__silnik == True:
            self.__predkosc += 10
            print(self.__predkosc)
            self.__biegWyzej()

    def hamuj(self):
        if self.__predkosc >= 10:
            self.__predkosc -= 10
        else:
            self.__predkosc = 0
        print(self.__predkosc)
        self.__biegNizej()