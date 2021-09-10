from random import randint

jogo = 'bingo'
cartela = [[],[],[],[],[]]
linha = '=-'*13

#gera os números da cartela aleatóriamente
for n in range(0,5):
    while len(cartela[n]) < 5:
        num = randint(1,15)
        if num not in cartela[n]: #se um número já estiver na cartela, procurar outro
            if n == 0:
                cartela[n].append(num)
            elif n == 1:
                cartela[n].append(num+15)
            elif n == 2:
                cartela[n].append(num+15*2)
            elif n == 3:
                cartela[n].append(num+15*3)
            elif n == 4:
                cartela[n].append(num+15*4)
    cartela[n].sort()

# substitui o numero do meio pelo J de Joker (coringas)
cartela[2][2] = 'J'

#apenas imprime o nome do jogo formatado para a cartela
for n in jogo:
    print(f'[{n.upper():^3}]',end='')

print(f'\n{linha}')

#renderiza a cartela na tela
for row in range(0,5):
    for col in range(0,5):
        print(f'[{str(cartela[col][row]):^3}]',end='')
    print()
