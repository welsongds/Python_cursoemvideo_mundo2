from datetime import date
nome = str(input('Insira seu nome: '))
nasc = int(input('Qual seu ano de nascimento: '))
gen = str(input('Qual seu gênero de nascimento (F/M): '))
ano = date.today().year
idade = ano - nasc
if gen == 'M':
    if idade == 18:
        print('Este é o ano ({}) do seu alistamento, corra pra fazer, {}.'.format(ano, nome))
    elif idade > 18:
        atraso = idade - 18
        print('Voce já deveria ter feito seu alistamente a {} ano(s), {}.'.format(atraso, nome))
    elif idade < 18:
        falta = 18 - idade
        print('Ainda faltam {} ano(s) para você se alistar, {}.'.format(falta, nome))
elif gen == 'F':
    print('Você não precisa se alistar!')
else:
    print('Você deve ter prenchido errado, tente novamente')
