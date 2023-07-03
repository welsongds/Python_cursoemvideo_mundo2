cmaiores = chomens = cmulheres = 0
while True:
    idade = int(input('Qual sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo de nascimento (M/F)? ')).upper().strip()[0]
    if idade >= 18:
        cmaiores += 1
    if sexo == 'M':
        chomens += 1
    if sexo == 'F' and idade < 20:
        cmulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar (S/N)? ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'{cmaiores} são maiores de idade, {chomens} são homens e {cmulheres} são mulheres com menos de 20 anos!')
