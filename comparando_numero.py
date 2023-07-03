num1 = int(input('Digite seu primeiro número: '))
num2 = int(input('Digite seu segundo número: '))
if num1 > num2:
    print('O maior é o primeiro número que você inseriu ({})!'.format(num1))
    print('O menor é o segundo ({})'.format(num2))
elif num1 < num2:
    print('O maior é o segundo número que você inseriu ({})'.format(num2))
    print('O menor é o primeiro ({})'.format(num1))
else:
    print('Não há maior ou menor, os números são iguais!')
