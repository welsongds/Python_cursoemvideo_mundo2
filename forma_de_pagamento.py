print('Calculando o valor do seu produto')
valor = float(input('Insira o valor do produto: '))
fpag = int(input("""As formas de pagamento são:
[1]À vista/cheque
[2]À vista no cartão
[3]Em até 2x no cartão
[4]3x ou mais no cartão
Insira o valor da sua opção: """))
if fpag == 1:
    pagar = valor - valor * 0.1
    print('Você pagará R${:.2f}, se você pagar à vista ou com cheque.'.format(pagar))
elif fpag == 2:
    pagar = valor - valor *0.05
    print('Você pagará R${:.2f}, se você pagar no cartão à vista.'.format(pagar))
elif fpag == 3:
    pagar = valor/2
    print('Você irá pagar em 2x de R${:.2f}, se dividir no cartão.'.format(pagar))
elif fpag == 4:
    vezes = int(input('Em quantas vezes você quer dividir: '))
    pagar = (valor + valor * 0.2)/vezes
    print('Você irá pagar R${:.2f} em {}x.'.format(pagar, vezes))
else:
    print('Opção não corresponde as opções!')
