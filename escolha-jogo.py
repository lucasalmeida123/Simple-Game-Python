def lin():
    print('-=' *27)

lin()
c = ''
print(f'{c:^15}ESCOLHA UM JOGO E DIVIRTASSE')
lin()
print(f'{c:^15}[ 1 ] JOKENPô [ 2 ] ADVINHÇÃO [ 3 ] Par ou Impar')
lin()
choose = int(input('FAÇA SUA ESCOLHA: '))
while choose != 1 and choose != 2 and choose != 3:
    escolha = int(input('FAÇA SUA ESCOLHA: '))

if choose == 1:
    import jokenpo
    __main__ = jokenpo
    
elif choose == 2:
    import jogo
    __main__ = jogo

elif choose == 3:
    import ParouImpar
    __main__ = ParouImpar
