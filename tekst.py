# artykul = '''
#             *** Mój program
#                 autor: Comarch
#         ...Tu będzie mój program...
#         -a tu będzie menu
#
# '''
#
# print(artykul)
#
# imie = 'Dominika'
# firma = 'Millennium'
#
# print(imie[0]) # pierwszy
# print(imie[-1]) # ostatni
# print(imie[0]+imie[-2]+imie[1:3])
# print(imie + firma[3:])
#
# print(firma.lower().count('m'))
# print(firma.upper().count('m'))
# print(firma.upper())
#
# print(len(firma))

imie = 'Dominika'
wiek = 25
print('Mam na imię %s' % imie)  # w miejsce s wpisz to co za %
print('Cześć, jestem %s, mieszkam w Kielcach. Mam %i lat' % (imie, wiek))

x=45.473576873574524857485
print('Liczba komet w okolicy Księżyca = %f' %x)
print('Liczba komet w okolicy Księżyca = %.2f' %x) #zaokrągla do 2 miejsc po przecinku
print('Liczba komet w okolicy Księżyca = %.1f' %x) #zaokrągla do 1 miejsca  po przecinku

print(f'mam na imię {imie}') # on juz sam formatuje na stringa

print('Lubię %(jezyk)s' % {'jezyk': 'Pythona'}) #tworzenie slownikow i kluczy, s - string
print('Lubię język {1} oraz {0}'.format('Java', 'Python'))

# %s = string
# %i = integer
# %f = float
# %x  lub %X - liczba szesnastkowa
