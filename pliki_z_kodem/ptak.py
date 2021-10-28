class Ptak: # klasa matka tez dziedziczy, od klasy glownej
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lec(self):
        print('Tu', self.gatunek, '. Startuje i zaraz osiagne predkosc', self.szybkosc)

    def wydajOdglos(self):
        pass


class Orzel(Ptak):

    def poluj(self):
        print('Tu', self.gatunek, '. Rozpoczalem polowanie')


class Pingwin(Ptak):

    def slizgaj(self):
        print('Tu', self.gatunek, '. Rozpoczalem slizganie')

    def lec(self): # nadpisanie metody, tylko w tym pingwinie ta metoda bedzie dzialac inaczej niz w orle i ptaku
        print('Tu', self.gatunek, '. Ja nie umiem latac')