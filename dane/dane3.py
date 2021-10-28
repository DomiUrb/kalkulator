import pandas as pd

#print(pd.read_csv('worldcities.csv'))
miasta = pd.read_csv('worldcities.csv')

miasta.to_excel('wynik_miasta.xlsx', sheet_name='miasta')
miasta.to_json('wynik_miasta_2.json')

