num = int(input('Digite um número qualquer [999 = parar]: '))
count = 0
somatorio = 0
while num != 999:
    somatorio += num
    num = int(input('Insira mais um número [999 = parar]: '))
    count += 1
print('O valor do somátorio foi {}, você digitou {} números.'.format(somatorio, count))
