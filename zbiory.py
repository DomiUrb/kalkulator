# przechowuje wylczanie unikalne elementy (usuwa duplikaty)
lotek = {23, 4, 5, 23, 13, 22, 23, 5}
kurs = {'Eliza', 'Olga', 'Zbyszek', 'Eliza', 'Olga'}
zbior = set(
    'pizza')  # dodaje pojedynczo, ale stringi rozbija na pojedyncze litery unikatowo i jeszcze w dowolnej kolejności dodaje, nie da sie zrobic sorta
zbior2 = set('pizzadiabolo')
print(zbior2 - zbior)  # roznica
print(zbior2.difference(zbior))
print(zbior2 | zbior)  # lub # suma
print(zbior2 & zbior)  # czesc wspolna # przeciecie
print(zbior2.intersection(zbior))  # czesc wspolna
print(zbior2 ^ zbior)  # roznica symetrzyczna

# print(lotek)
# print(kurs)
# print(zbior)
# print(zbior2)
