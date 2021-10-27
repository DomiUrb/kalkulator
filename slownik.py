slownik = {}
slownik = dict([('jeden', 1), ('dwa', 2), ('trzy', 3)])
slownik2 = dict(jeden = 1, dwa = 2, trzy = 3)
slownik3 = {'cztery':4, 'pięć':5}

slownik

#print(slownik3)

print('jeden' in slownik2)
print(slownik2.keys()) #printuje klucze ze slownika
print(slownik2.values()) #printuje wartosci ze slownika

slownik2['cztery'] = 4 #dodawanie kluczy i wartości do slownika
print(slownik2.keys()) #printuje klucze ze slownika