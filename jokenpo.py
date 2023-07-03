import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
usua = int(input('''ESCOLHA SUA OPÇÃO:
[0]Pedra
[1]Papel
[2]Tesoura
Qual sua opção: '''))
comp = random.randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 11)
print('Você jogou {}'.format(itens[usua]))
print('Computador jogou {}'.format(itens[comp]))
print('-=' * 11)
if comp == usua:
    print('Deu empate!')
elif usua == 0:
    if comp == 1:
        print('O computador venceu!')
    elif comp == 2:
        print('O usúario venceu!')
elif usua == 1:
    if comp == 2:
        print('O computador venceu!')
    elif comp == 0:
        print('O usuário venceu!')
elif usua == 2:
    if comp == 0:
        print('O computador venceu')
    elif comp == 1:
        print('O usuário venceu!')
else:
    print('Seu comando não é válido!')
