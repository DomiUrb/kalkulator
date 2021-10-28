import pandas as pd

# print(pd.read_excel('imiona.xlsx'))
# print(pd.read_csv('Halloween.csv'))

# zbior = pd.DataFrame()
# print(zbior)

lista = [[1, 2, 5, 7], [11, 22, 33, 44], [55, 33, 99, 0]]
lista1 = pd.DataFrame(lista)
lista1.columns = ['Liczby', 'Liczby2', 'Liczby4', 'Liczby4']
# print(lista1)

slownik = {'Imie': ['Ania', 'Michał', 'Przemek'], 'Wiek': [18, 25, 40], 'Plec': ['k', 'm', 'm']}
# print(pd.DataFrame(slownik))

s = pd.Series([11, 55, 66, 99])  # series - jednokolumnowy
# s = pd.Series(lista)
# print(s)
pd.DataFrame(s)
print(pd.DataFrame(s))
