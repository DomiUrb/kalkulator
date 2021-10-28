from abc import ABC, abstractmethod


class Ptak(ABC): # klasa matka tez dziedziczy, od klasy glownej
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lec(self):
        print('Tu', self.gatunek, '. Startuje i zaraz osiagne __predkosc', self.szybkosc)

    @abstractmethod # wymusza! nadpisanie przez każdego potomka (mozna nie uzywac tego abstraktu i po prostu nadpisac), to zeby zaznaczyc, ze trzeba w potomkach nadpisuywac ten odglos
    def wydajOdglos(self):
        pass


class Orzel(Ptak):

    #nadpisujemy konstruktra
    def __init__(self, szybkosc):
        super().__init__('Orzeł', szybkosc) #przy tworzeniu orla najpierw wywoal sie to, co ma super


    def poluj(self):
        print('Tu', self.gatunek, '. Rozpoczalem polowanie')

    def wydajOdglos(self):
        print('aaa')


class Pingwin(Ptak):

    # def __init__(self, szybkosc):
    #     super().__init__('Pingwin', szybkosc)

    def __init__(self):
        super().__init__('Pingwin', 0) # teraz mozna wywolywac bez parametrow, tylko w tym super init trzeba podac te parametry, ktore maja byc zawsze uzyte

    def slizgaj(self):
        print('Tu', self.gatunek, '. Rozpoczalem slizganie')

    def lec(self): # nadpisanie metody, tylko w tym pingwinie ta metoda bedzie dzialac inaczej niz w orle i ptaku
        print('Tu', self.gatunek, '. Ja nie umiem latac')

    def wydajOdglos(self):
        print('kwii')