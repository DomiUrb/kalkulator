import random
import time

# wyniki
user = 0
computer = 0

while True:
    x = input('Wpisz wybór:')
    if x == 'x':
        break
    elif x == 'o':
        x = 'orzeł'
    elif x == 'r':
        x = 'reszka'
    else:
        print('Proszę dokonać prawidłowego wyboru')
        print('o - orzeł')
        print('r - reszka')
        print('x - koniec gry')
        continue #obsluga bledu

    y = random.choice(["orzeł", "reszka"])

    for i in range(0, 3):
        print(3 - i)
        time.sleep(1) #uspic program na sekunde, odliczanie takie tu sie robi

    print('Wynik rzutu: ', y)

    if x == y:
        user += 1
    else:
        computer += 1

    print('Wyniki gry:')
    print('Użytkwonik:', user)
    print('komputer:', computer)