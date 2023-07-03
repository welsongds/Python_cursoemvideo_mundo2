c = soma = 0
while True:
    n = int(input('Digite um número (999 =  PARAR): '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'Você digitou {c} números e a soma entre eles foi {soma}!')
