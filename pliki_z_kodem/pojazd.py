# nazwy klas zwyczajowo zaczynają sie z duzej litery i sa mozliwie krotkie
class Pojazd:
    '''
    Jest to klasa opisująca pojazd
    '''

    def __init__(self, kolor, marka): #tu podajemy wszystkie elementy, z ktorych bedzie pojazd korzystal
        '''konstruktor'''
        self.kolor = kolor
        self.marka = marka

    def hamuj(self): # teraz definiujemy czynnosci: hamuj, jedz itd
        print('Hamuje...')

    def jedz(self):
        print('%s jedzie dalej...' % self.marka)


pojazd1 = Pojazd('czerwony', 'BMW')

pojazd1.jedz()
pojazd1.hamuj()

pojazd2 = Pojazd('niebieski', 'audi')

pojazd2.jedz()

