from random import randint
cv = 0
while True:
    comp = randint(0, 10)
    usu = int(input('Digite um número: '))
    total = comp + usu
    usuparimpar = ''
    while usuparimpar not in 'PI':
        usuparimpar = str(input('Você deseja par ou ímpar (P/I): ')).upper().strip()[0]
    print(f'Você jogou {usu} e o computador jogou {comp}. Total de {total}', end= '')
    print('Deu par' if total % 2 == 0 else 'Deu ímpar')
    if usuparimpar == 'P':
        if total % 2 == 0:
            print('You win')
            cv += 1
        else:
            print('You lose')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('You win')
            cv += 1
        else:
            print('You lose')
            break
    print('Vamos jogar novamente...')
print(f'Você perdeu, mas teve {cv} vitória(s)!')
