from random import randint
from time import sleep

numeros = []
while len(numeros) < 75:
    num = randint(1,75)
    if num not in numeros:
        numeros.append(num)

def numSort(t=''):
    for n in numeros:
        if t == '':            
            print(n)
            sleep(1)
        else:
            print(n)
            sleep(t)

numSort()

