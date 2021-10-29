# zapis do bazy danych - SQL
import pandas as pd
import sqlite3 as sql

film = pd.read_csv('film(20211028_141857).csv', sep=';', encoding='ISO-8859-1',
                   skiprows=[1], dtype={'Year': 'int64','Length': 'float64', 'Popularity': 'float64'},
                   usecols=['Year', 'Length', 'Title', 'Awards', 'Popularity'],
                   converters={'Awards': lambda x: True if x == 'Yes' else 'False'} #converters={'Awards': zamien}) a do tej lambdy to zamien jest niepotrzebny
                   )

connect = sql.connect('new.sqlite') # nazwa bazy
#film.to_sql('filmy', connect) # zapisanie do tabeli filmy

movies = pd.read_sql('select * from filmy where Year > 1995', connect)

print(movies)