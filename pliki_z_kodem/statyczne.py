class Licznik:
    ile = 0  # pole statyczne, poza initem!

    def __init__(self):
        Licznik.ile += 1  # odwolanie do pola statycznego
        self.ktory = Licznik.ile
        print(f'To jest obiekt nr {Licznik.ile}')

    # destruktor, on dziala zawsze na koncu! to wszystko, cala procedura niszczenia i tak sie dzieje, ale to tylko, zeby wyprintowac co sie tam dzieje
    def __del__(self):
        Licznik.ile -= 1
        print(f'niszcze obiekt nr {self.ktory}, pozostalo jeszcze {Licznik.ile}')

    @staticmethod #metoda statyczna dekorator, do modyfikacji funkcji
    def policz():
        return Licznik.ile


def main():
    a = Licznik()
    b = Licznik()
    c = Licznik()
    print(f'a to obiekt nr {a.ktory}')
    print(f'b to obiekt nr {b.ktory}')
    print(f'c to obiekt nr {c.ktory}')
    print(f'Liczba obiektow to: {Licznik.policz()}') # po tym wchodzi destruktor
    a = None
    b = None
    print(f'Liczba obiektow to: {Licznik.policz()}')


if __name__ == "__main__":
    main()
