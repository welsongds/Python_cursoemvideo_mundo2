c = 0
termo = 0
pt = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
while c <= 9:
    termo = pt + c * rz
    print('O {}° termo tem valor de {}'.format(c+1, termo))
    c += 1
print('END')
