s = 0
n = int(input('Insira um número: '))
for c in range(1, n+1):
    if n % c == 0:
        s = s + 1
if s == 2:
    print('Esse é um número primo.')
    print('Só e dividido por 1 e por ele mesmo')
else:
    print('Esse não é um número primo.')
    print('Ele é divísivel por {} números.'.format(s+2))
