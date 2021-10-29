# apply - funkcja ktora bedzie cos wykonywacna danej kolumnie w tabeli
import pandas as pd

df = pd.DataFrame({'Osoba': ['Michał Jakub', 'Ewa Noga', 'Krzysztof Zawierucha'],
                   'Wynik': [15, 38, 21]})


def sprawdz(punkty):
    if punkty > 20:
        return 'Zdany'
    else:
        return 'Oblany'

def rozdziel(wiersz):
    wiersz['Imie'], wiersz['Nazwisko'] = wiersz['Osoba'].split(' ')
    return wiersz


#df.Wynik = df.Wynik.apply(sprawdz)
#df = df.apply(rozdziel, axis = 1)
print(df)

# Axis along which the function is applied:
#
# 0 or ‘index’: apply function to each column.
#
# 1 or ‘columns’: apply function to each row.