class Czlowiek:
    def __init__(self, imie, wiek, plec): # dziala klasa bez konstruktra, ale lepiej zrobic z konstruktorem,, bo potem latwiej korzystac z klasy
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def przywitaj(self):
        print('Czesc mam na imie', self.imie)

    def ruszaj(self):
        if self.plec=='k':
            print('Ruszylam')
        else:
            print('Ruszylem')

    def mysl(self):
        if self.wiek < 2:
            print('Ja dopiero sie ucze')
        else:
            print('Juz sobie mysle')
