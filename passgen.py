import random
x = int(input('wpisz, jak dlugie ma byc haslo'))
a = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sp = ""

for i in range(x):
    sp += random.choice(a)
print(sp)
