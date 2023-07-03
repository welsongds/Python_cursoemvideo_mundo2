num = int(input('Insira o primeiro número: '))
somatorio = 0
count = 1
maior = 0
menor = num
continuar = ''
while continuar != 'N':
    somatorio += num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    continuar = str(input('Você deseja inserir mais um número (S/N): ')).upper().strip()[0]
    if continuar == 'S':
        num = int(input('Digite mais um número: '))
        count += 1
print('O maior valor foi {}, o menor foi {} e a média é {}.'.format(maior, menor, somatorio / count))
