from datetime import date
maiores = 0
menores = 0
for c in range(0, 7):
    nasc = int(input('Qual o ano de nascimento da {}° pessoa: '.format(c+1)))
    idade = date.today().year - nasc
    if idade >= 18:
        maiores = maiores + 1
    elif idade < 18:
        menores = menores + 1
print('Entre essas pessoas, {} são maiores de idade e {} menores de idade.'.format(maiores, menores))
