c = 0
termo = 0
ex = 0
pt = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
qt = int(input('Quantos termos você deseja: '))
while c <= qt:
    termo = pt + c * rz
    print('O {}° termo tem valor de {}'.format(c+1, termo))
    c += 1
    if c == qt:
        ex = int(input('Você deseja mais quantos termos: '))
        if ex >= 1:
            qt += ex
        else:
            break
print('END')
