from math import factorial
num = int(input('Insira o valor o qual você deseja descobrir o calculo fatorial: '))
c = num
f = factorial(num)
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(f))
print('END')
