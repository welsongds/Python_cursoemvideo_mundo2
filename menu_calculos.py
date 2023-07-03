num1 = int(input('Qual o primeiro número: '))
num2 = int(input('Qual o segundo número: '))
opc = 0
while opc != 5:
    opc = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Insira sua opção: '''))
    if opc == 1:
        print('A soma de {} e {}, tem por resultado: {}'.format(num1, num2, num1 + num2))
    elif opc == 2:
        print('A multiplicação entre {} e {}, tem por resultado: {}'.format(num1, num2, num1 * num2))
    elif opc == 3:
        if num1 > num2:
            print('O valor {} é maior que {}.'.format(num1, num2))
        elif num2 > num1:
            print('O valor {} é maior que {}.'.format(num2, num1))
        elif num1 == num2:
            print('Os números são iguais')
    elif opc == 4:
        num1 = int(input('Insira um novo primeiro valor: '))
        num2 = int(input('Insira um novo segundo valor: '))
    elif opc > 5:
        print('Opção inválida!')
print('END')
