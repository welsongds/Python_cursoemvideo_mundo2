termo = 0
pt = int(input('Digite qual será seu primeiro termo: '))
rz = int(input('Digite o valor da sua razão: '))
print('O 1° termo é {}'.format(pt))
for c in range(1,10):
    termo = pt + rz * c
    print('O {}° termo é {}'.format(c+1, termo))
print('FIM')
