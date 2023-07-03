nota1 = float(input('Insira sua primeira nota aqui: '))
nota2 = float(input('Insira sua segunda nota aqui: '))
med = (nota1+nota2)/2
if med < 5.0:
    print('Infelimente você foi REPROVADO, sua média foi: {:.2f}.'.format(med))
elif 5.0 <= med <= 6.9:
    print('Você deverá fazer a RECUPERAÇÃO, sua média foi {:.2f}.'.format(med))
elif med >= 7:
    print('Você foi APROVADO, com a média: {:.2f}'.format(med))
