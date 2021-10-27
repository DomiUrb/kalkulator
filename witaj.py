print('cześć')
print('2 + 21 =', 2 + 21)

# nie trzeba deklarować typu zmiennych
imie = 'Tomasz'
praca = 'Comarch'
wiek = 39
CzyPali = False  # kebab case - rozdzielanie podkreslnikami, cammel case - np: CzyPali
wzrost = 1.77

print('wzrost: ', wzrost)
print(wiek + wzrost)  # przy dodawaniu musza byc te same typy danych, nie mozna dodac liczby do stringa
print(imie + praca)  # nie dodaje spacji miedzy wyrazami
print(imie + ' ' + praca)  # nie dodaje spacji miedzy wyrazami
print(imie, praca)  # uwzględnia spacje

print(type(imie))
print(type(wiek))
print(type(CzyPali))
print(type(wzrost))
