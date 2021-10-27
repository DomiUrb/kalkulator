import time

czas = time.localtime()
print(czas[3], czas[4], czas[5], sep=':')

print('Godzina', czas[3])

data = time.strftime("%Y %B %d, %H:%M:%S", time.localtime())
print(data)