# from pakiet import *
# from pliki_z_kodem import rzutowanie
# import pyfiglet
# import random
#from pliki_z_kodem.pojazd import Pojazd, FordMustang
#from pliki_z_kodem.human import Czlowiek
from pliki_z_kodem.ptak import Ptak, Orzel, Pingwin


if __name__ == "__main__":  # zeby uruchomic tylko to, co jest w mainie a nie wszxystjkoe, co jest za zaimportowane
    print('Witaj w moim programie')
    # pakiet.witaj()
    #print(10 != 'tekst' and 12 > 3)
    #print(random.randint(1,3)<5 and random.randint(1,10)==11)
    #print('kajak'.find('jak'))


    # pojazd1 = Pojazd('czerwony', 'BMW')
    # pojazd1.jedz()
    # pojazd1.hamuj()
    #
    # pojazd2 = Pojazd('niebieski', 'audi')
    # pojazd2.jedz()
    #
    # pojazd3 = FordMustang('czarny', 'ford')
    # pojazd3.jedz()
    # pojazd3.hamuj()
    # pojazd2.hamuj()
    #
    # print(pojazd3.sygnal)
    # input('Wcisnij ENTER aby zakonczyc...')

    # a = input('Wpisz tekst')
    # if a.find('!') >= 0 or a.find('@') >=0:
    #     print ('Znalazlem znak')
    # else:
    #     print('Brak znakow spec')

# auto1 = Pojazd('niebieski', 'bmw')
# print(auto1.jedz())

# ludzik1 = Czlowiek('Domi', 'k', 25) # dla klasy bez konstruktora trzeba definiowac osobno argumenty:
# ludzik1.przywitaj()

o=Orzel('Orzeł', 80)
p=Pingwin('Pingwin', 30)

o.lec()
p.lec()
o.poluj()