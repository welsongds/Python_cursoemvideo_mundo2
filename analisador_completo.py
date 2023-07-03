somida = 0
maisvelhomome = ''
maisvelhoidade = 0
mlrplus = 0
for c in range(0, 4):
    print('Informações da {}° pessoa'.format(c+1))
    nome = str(input('Qual seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu gênero (M/F)? ')).strip().upper()
    somida += idade
    if sexo == 'F' and idade >= 20:
        mlrplus = mlrplus + 1
    elif  sexo == 'M' and maisvelhoidade < idade:
        maisvelhomome = nome
        maisvelhoidade = idade
print('A média de idades foi {:.2f}.'.format(somida/4))
print('A quantidade de mulheres com mais de 20 anos foi {}.'.format(mlrplus))
print('O nome do homem mais velho foi {}.'.format(maisvelhomome))
