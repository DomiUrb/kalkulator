import re #regexp
'''
Wyrażenie regularne Opis
a | b a lub b
. jakikolwiek znak (dokladnie jeden!) z wyjątkiem nowego wiersza
^ początek wiersza
$ koniec wiersza
* 0 lub więcej wystąpień poprzedzającego wyrażenia
+ 1 lub więcej wystąpień poprzedzającego wyrażenia
? 0 lub 1 wystąpienie poprzedzającego wyrażenia
{n} n wystąpień poprzedzającego wyrażenia
{m, n} od m do n wystąpień poprzedzającego wyrażenia
\d cyfra
\w znak alfanumeryczny
\s spacja, tabulator, znak końca linii/nowego wiersza
'''

#tekst = input('Podaj tekst: ') # np Python
#
#r = re.match('P.t', tekst) #najpierw wzor(pattern) -> w kropeczke wrzuci to, co znajdzie miedzy P i t w tekst, dokladnie
#print(r.group())

# r = re.search('.t.', tekst) # pokazuje znaki przed i po t
# print(r.group())

# wyr = 'hun|han|hon'
# tekst = input('Podaj tekst: ')
#
# # r = re.search(wyr, tekst)
# # print(r.group())
#
# r = re.findall(wyr, tekst)
# print(r)

# wyr = '^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$' # mail
# wyr3 = '^\d{11}$' # pesel
# wyr4 = '\d{2}[ ]\d{4}[ ]\d{4}[ ]\d{4}[ ]\d{4}[ ]\d{4}[ ]\d{4}.'#NBR
# tekst = input('Podaj tekst: ')
#
# r = re.findall(wyr, tekst)


tekst = """Wyobraz sobie, ze ten tekst zawiera numer
PIN 9434 twojej karty do bankomatu, a ty wlasnie go
zapomniales. Jak szybko go odnalezc?"""

sciezka = r'\d\d\d\d'
dopasowanie = re.search(sciezka, tekst)

if dopasowanie: #Sprawdzamy czy udalo sie cos znalezc
    numer = dopasowanie.group()
    print (numer)
