s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('O valor do somatório é {}'.format(s))
print('Foi somando {} números.'.format(cont))
