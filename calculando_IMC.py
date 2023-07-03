alt = float(input('Insira sua altura (m): '))
peso = float(input('Insira seu peso (kg): '))
imc = peso / alt ** 2
if imc < 18.5:
    print('Você se encontra abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Você se encontra no peso ideal.')
elif 25 < imc <= 30:
    print('Você se encontra com sobrepeso.')
elif 30 < imc <= 40:
    print('Você se encontra obeso.')
elif 40 < imc:
    print('Você se econtra na Obesidade Mórbida.')
print('Seu IMC = {:.2f}'.format(imc))
