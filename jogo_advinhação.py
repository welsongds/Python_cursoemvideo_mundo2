import random
tent = 0
num = random.randint(0, 10)
usuario = 11
print('Vamos começar nosso jogo, o computador já escolheu o número entre 0 e 10.')
while num != usuario:
    usuario = int(input('Tente advinhar o número: '))
    tent += 1
    if num > usuario:
        print('Tente um número maior!')
    elif num < usuario:
        print('Tente um número menor!')
print('Finalmente você acertou, precisou de {} tentativas para acertar!'.format(tent))
