from random import randint 
armas = ('PEDRA', 'PAPEL', 'TESOURA')
empate = 0
cv = 0
pv = 0


def lin():
    print('-=' * 20)


c = ''
lin()
print(f'{c:^10}VAMOS JOGAR JOKENPÔ')
lin()
print('[ 0 ] PEDRA \n[ 1 ] PAPEL\n[ 2 ] TESOURA')
lin()
print(f'{c:^10}\033[0;31;0mVOCÊ TEM 3 VIDAS\033[m')
lin()
while True:
    computer = randint(0, 2)
    player = int(input('Faça sua jogada: '))
    print(f'JOGADOR : {armas[player]} X {armas[player]}')
    if player == computer:
        print('EMPATE', end=' ')
        empate += 1
    if player == 0:
        if computer == 1:
            print('computador venci: ' , end=' ')
            cv +=1
        elif computer == 2:
            print('Jogador venci: ' ,end='')
            pv += 1
    if player == 1:
        if computer == 0:
            print('Jogador venci: ' ,end='')
            pv += 1
        elif computer == 2:
            print('computador venci: ' , end=' ')
            cv += 1

    if player == 2:
        if computer == 1:
            print('Jogador venci: ',end='')
            pv += 1
        elif computer == 0:
            print('computador venci: ', end=' ')
            cv +=1

    if cv == 3:
        break
print(f'{pv} Vitorias. {cv} Derrotas. {empate} Empates')
