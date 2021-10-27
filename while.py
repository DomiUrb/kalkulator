# while True: # to jest petla nieskonczona! mozna zatrzymac ctrl+c albo stopem w gornym prawym roku
#     print('To ja - pętla, aby mnie zabić, wciśnij ctrl+c')

# licznik = 0
# while True:
#     licznik +=1
#     print(licznik)
#     if licznik > 10:
#         break # wychodzenie z pętli


lista = []
print('Podaj liczby...')
print('Wpisz "stop" aby zakonczyc...')

while True:
    wejscie = input()
    if wejscie == 'stop':
        break
    lista.append(int(wejscie))
print('Twoja lista: ' + repr(lista)) # reprint rzutowanie na stringa, mozna inaczej: print ('Twoja lista: ', lista)
