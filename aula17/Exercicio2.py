
from random import randint
aleatorio = randint(1,10)

numero = 0

while not numero == aleatorio:
    numero = int(input('Digite um numero : '))
    if numero > aleatorio:
        print('O numero é menor! ')
    elif numero < aleatorio:
        print('O numero é maior! ')
else:
    print('Você acertou!!! ')




