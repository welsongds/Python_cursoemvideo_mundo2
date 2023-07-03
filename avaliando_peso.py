maior = 0
menor = 99999999999
for c in range(0, 5):
    peso = float(input('Insira o peso da {}° pessoa: '.format(c+1)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso foi {}kg e o menor foi {}kg'.format(maior, menor))
