import pandas as pd

kostium = pd.read_csv('Halloween.csv', header=2)  # header = 2 -> naglowki kolumn sa w drugim wierszu

# print(kostium.head()) #piec pierwszych wierszy

# print(kostium[:10][['region', '1']]) # 10 pierwzych wierszyz wybr kolumn

# modyfikacja danych w pliku
# kostium[3:4]['1'] = 'Batman' # tak sie nie da

# print(kostium.index)

# print(kostium.region.is_unique) # spr czy kolumna region jest unikalna

# zeby indeksem stał sie region

kostium.set_index('region', inplace=True)  # region stal sie indeksem, ale to musi byc unikatowa kolumna -> ale to tylko tak dziala, tdopoki nie jest odznaczone
#kostium.reset_index('region', inplace=True) # resetuje i przywraca poczatkowy indeks, ale jak odznacze powyzszy wiersz, to samo wroci do ustawien poczatkowych
# print(kostium) #piec pierwszych wierszy
# print(kostium[:10][['1', '2', '3', '4', '5']])
#print(kostium[:10][['1']])

#print(kostium.loc[:10][['1']]) #lock dziala na bazie indeeksacji, ale w taki sposob z : -> tylko na integerach (na sytringach -> trzeba wpisach string), wskazuje lokalizacje
#print(kostium.loc['Florida'][['1']])
#print(kostium.loc['Florida'][['1','2', '3', '4', '5']])
kostium.loc['Florida','1'] = 'Batman'
print(kostium.loc['Florida'][['1']])


