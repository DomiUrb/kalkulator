import pandas as pd


def zamien(wartosc):
    if wartosc == 'No':
        return False
    if wartosc == 'Yes':  # uwaga, moze wyjsc z funkcji jak pozamienia No, dlatego lepeij 2x if
        return True


# film = pd.read_csv('film(20211028_141857).csv', sep=';', encoding='ISO-8859-1')

film = pd.read_csv('film(20211028_141857).csv', sep=';', encoding='ISO-8859-1',
                   skiprows=[1], dtype={'Length': 'float64', 'Popularity': 'float64'},
                   converters={'Awards': lambda x: True if x == 'Yes' else 'False'} #converters={'Awards': zamien}) a do tej lambdy to zamien jest niepotrzebny
                   )

film = film.drop(0)  # usuwa pierwszy wiersz
film = film.drop(columns=['*Image'])  # usuwa kolumne *Image
# print(film)

# print(film.Length.mean()) # srednia z liczb w kolumnie
# print(film.info())
# film.Length = pd.to_numeric(film.Length) # zamienia typ danych ze wskazanej kolumny
# print(film.info())
# print(film.Length.mean())

# film.Length = film.Length.astype('float64') #inny sposob na zamiane typow danych we wskazanej kolumnie
# print(film.info())


# film.Awards = film.Awards.apply(zamien)
print(film)
