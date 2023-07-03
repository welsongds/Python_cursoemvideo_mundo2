print('Sequência de Fibonacci')
seq = int(input('Quantos números você quer na sequencia: '))
t1 = 0
t2 = 1
t3 = t1 + t2
ultimo = t3
penultimo = t2
cont = 3
print('{} -> {} -> {} -> '.format(t1, t2, t3), end='')
while cont <= seq:
    resultado = ultimo + penultimo
    penultimo = ultimo
    ultimo = resultado
    cont += 1
    print(resultado, end=' -> ')
print('FIM')