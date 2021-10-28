import pandas as pd

#print(pd.read_excel('imiona.xlsx')) # domyslnie odczytuje tylko pierwsza zakladke
imiona = pd.read_excel('imiona.xlsx')
#print(pd.read_excel('imiona.xlsx', sheet_name='Wynik', header=1))

print(pd.read_excel('imiona.xlsx', sheet_name='Wynik2', header=None, names= ['Imie', 'Nazwisko', 'Wynik']))