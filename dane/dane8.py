import pandas as pd

film = pd.read_csv('film(20211028_141857).csv', sep=';', encoding='ISO-8859-1',
                   skiprows=[1], dtype={'Year': 'int64','Length': 'float64', 'Popularity': 'float64'},
                   usecols=['Year', 'Length', 'Title', 'Awards', 'Popularity'],
                   converters={'Awards': lambda x: True if x == 'Yes' else 'False'}, #converters={'Awards': zamien}) a do tej lambdy to zamien jest niepotrzebny
                   )

#print(film.groupby('Year').count()) # grupowanie
#print(film.groupby('Year').Popularity.mean()) # srednia w kol Popularity frupowanie po roku, mozna sum() itd
#print(film.groupby(['Year', 'Awards']).Length.mean()) # srednia w kol Popularity frupowanie po roku, mozna sum() itd

#agregat
#print(film.groupby('Year').agg({'Popularity':['min','max'], 'Length':['min','max']})) # srednia w kol Popularity frupowanie po roku, mozna sum() itd
#print(film.groupby('Year').agg({'Popularity':'sum', 'Length':'mean'})) # srednia w kol Popularity frupowanie po roku, mozna sum() itd

#print(film.groupby('Year').agg(min_dl=('Length', 'min'), max_dl=('Length', 'min'))) # srednia w kol Popularity frupowanie po roku, mozna sum() itd

#filtry
print(film[(film['Year'] > 1980) & (film['Year'] <= 1990)].groupby('Year').Length.mean()) # filtr, group by  i srednia


#print(film)