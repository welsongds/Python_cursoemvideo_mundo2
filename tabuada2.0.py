n = int(input('De qual número você deseja a tabuada: '))
for c in range(0,11):
    r = c * n
    print(' {} x {} = {}'.format(c, n, r))
print('Essa é a tabuada do número {}.'.format(n))
