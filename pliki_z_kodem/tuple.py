# krotki - listy niemutowalne (niezmienialne)
menu = ('hamburger', 'hotdog', 'pizza')
print(menu)
zamowienie = menu[2:]
print(zamowienie)

noweMenu = list(menu)  # rzutujemy krotke na liste i juz jest edytowalna, oryginalne menu (krotka) sie nie zmienia
menu3 = tuple(noweMenu) # rzutowanie listy na krotke