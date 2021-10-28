import pandas as pd

miasta = pd.read_csv('worldcities.csv')

#print(miasta.head(10))  # bez argumentu daje 5 pierwszych wierszy, ale mozna sobie ustawic inaczej
#print(miasta[:5]) # to samo co wyzej
#print(miasta.tail()) # 5 ostatnich
#print(miasta['city'] # dane tylko z wymienionych kolumn
#print(miasta[['city', 'capital', 'id']]) # dane tylko z wymienionych kolumn
#print(miasta[:5]['city']) # to samo co wyzej

#print(miasta.shape) # wymiary pliku
#print(miasta.info()) #szczegolowy opis pliku

#print(miasta.describe())  # szczegoly i statystyki dla kolumn liczbowych

print(miasta.population.describe())