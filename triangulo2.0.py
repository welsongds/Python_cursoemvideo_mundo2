print('Vamos formar um triângulo')
l1 = int(input('Insira o primeiro lado do triângulo: '))
l2 = int(input('Insira o segundo lado do triângulo: '))
l3 = int(input('Insira o terceiro lado do triângulo: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    if l1 == l2 == l3:
        print('Esse é um triângulo equilátero, tem todos os lados iguais.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Esse é um triângulo isósceles, tem dois lados iguais')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('Esse é um triângulo escaleno, tem todos os lados diferentes.')
else:
    print('Não é um triângulo!')
