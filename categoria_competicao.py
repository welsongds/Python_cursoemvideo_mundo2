from datetime import date
nome = str(input('Insira seu nome: '))
anonasc = int(input('Insiera o ano do seu nascimento: '))
idade = date.today().year - anonasc
if idade <= 9:
    print('Você se encaixa na categoria MIRIM, {}.'.format(nome))
elif 9 < idade <= 14:
    print('Você se encaixa na categoria INFANTIL, {}'.format(nome))
elif 14 < idade <= 19:
    print('Você se encaixa na categoria JUNIOR, {}'.format(nome))
elif 19 < idade <= 25:
    print('Você se encaixa na categoria Sênior,{}'.format(nome))
else:
    print('Você se encaixa na categoria MASTER, {}'.format(nome))
