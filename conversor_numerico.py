print('BEM VINDO AO NOSSO CONVERSOR NUMÉRICO')
num = int(input('Qual número você deseja transformar? '))
print('''Escolha dentre nossas opções
[0]Transformar em binário
[1]Transformar em octal
[2]Transformar em hexadecimal
[3]Todas as opções''')
opc = int(input('Qual das opções você deseja: '))
if opc == 0:
    print('Seu número era {} e na forma binária fica {}.'.format(num, bin(num)[2:]))
elif opc == 1:
    print('Seu número era {} e na forma octal fica {}.'.format(num, oct(num)[2:]))
elif opc == 2:
    print('Seu número era {} e na forma hexadecimal fica {}.'.format(num, hex(num)[2:]))
elif opc == 3:
    print('Seu número era {}, binário={}, octal={}, hexadecimal={}'.format(num, bin(num)[2:], oct(num)[2:], hex(num)[2:]))
else:
    print('Este número não está entre as opções! Try again :(')
