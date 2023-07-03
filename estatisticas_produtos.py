somatorio = contacaro = menor = cont = 0
nomemenor =''
while True:
    nome = str(input('Qual o nome do produto: '))
    valor = float(input('Qual o valor do produto: R$ '))
    cont += 1
    if cont == 1 or menor > valor:
        menor = valor
        nomemenor = nome
    somatorio += valor
    if valor > 1000:
        contacaro += 1
    continuar = ' '
    while continuar not in 'SN' :
        continuar = str(input('Você deseja adicionair mais produtos (S/N): ')).upper().strip()[0]
    if continuar == 'N':
            break
print(f'O total é R${somatorio}, {contacaro} produto(s) custa(m) mais de R$1000,00 e o produto mais barato é {nomemenor}')
