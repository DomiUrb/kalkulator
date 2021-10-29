import pandas as pd

kostium = pd.read_csv('Halloween.csv', header=2)  # header = 2 -> naglowki kolumn sa w drugim wierszu
#print(kostium.head()) #piec pierwszych wierszy


# print(kostium[:10][['region', '1']]) # 10 pierwzych wierszyz wybr kolumn

# modyfikacja danych w pliku
# kostium[3:4]['1'] = 'Batman' # tak sie nie da

# print(kostium.index)

# print(kostium.region.is_unique) # spr czy kolumna region jest unikalna

# zeby indeksem stał sie region

# kostium.set_index('region', inplace=True)  # region stal sie indeksem, ale to musi byc unikatowa kolumna -> ale to tylko tak dziala, tdopoki nie jest odznaczone
# kostium.reset_index('region', inplace=True) # resetuje i przywraca poczatkowy indeks, ale jak odznacze powyzszy wiersz, to samo wroci do ustawien poczatkowych
# print(kostium) #piec pierwszych wierszy
# print(kostium[:10][['1', '2', '3', '4', '5']])
# print(kostium[:10][['1']])

# print(kostium.loc[:10][['1']]) #lock dziala na bazie indeeksacji, ale w taki sposob z : -> tylko na integerach (na sytringach -> trzeba wpisach string), wskazuje lokalizacje
# print(kostium.loc['Florida'][['1']])
# print(kostium.loc['Florida'][['1','2', '3', '4', '5']])
# kostium.loc['Florida','1'] = 'Batman'
#kostium.loc[9, '1'] = 'Batman'
# print(kostium.iloc[9,1])
# print(kostium.loc['Florida'][['1']])
# print(kostium)

# for index, zawartosc in kostium.iterrows():
#     if zawartosc['1'] == 'Rabbit':
#         print(zawartosc['region'])

# print(kostium[kostium['1'] == 'Rabbit']) # wyswietla wszystkie wiersze, gdzie w kol 1 jest Rabbit -> w tabele wkladamy tabele maskowana
# print(kostium[(kostium['1'] == 'Rabbit') | (kostium['1'] == 'Batman')]) # | -> lub (pipe), nie mozna stosowac slownie or
# print(kostium[(kostium['1'] == 'Rabbit') & (kostium['3'] == 'Ninja')]) # & -> i

# modyfikacje kolumn

kostium['Nowa'] = '0' # wstawia nowa kolumne na koncu
kostium.loc[kostium['1'] == 'Rabbit', 'Nowa'] = 'X' # tam gdzie w pierwszej kol rabbit - wstaw w Nowa X
#print(kostium.rename(columns={'1':'Kol1', '2':'Kol2'})) # zmiana nazw kolumn printowac w  locie
#print(kostium)

#usuwanie kolumn
#print(kostium.drop('Nowa', axis = 1)) # axis1 -> kasuje kolumne, nie wiersz

#scalanie komorek
kostium['Polaczone'] = kostium['2']+ ' | ' + kostium['3']
#print(kostium.head())

# rozcalanie, rozłaczanie

kostium[['Trzeci', 'Czwarty']] = kostium.Polaczone.str.split('|', expand = True)
print(kostium.head())

#apply - funkcja ktora bedzie cos wykonywac dla rekordow w tabeli