from random import randint

sorteio = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
print(sorteio)

organizada = sorted(sorteio)

print(f'O menor valor foi {organizada[0]} e o maior valor foi {organizada[4]}')