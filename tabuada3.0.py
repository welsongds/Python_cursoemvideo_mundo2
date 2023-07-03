from time import sleep
while True:
    num = int(input('Digite o número que você deseja a tabuada: '))
    if num < 0:
        print('Encerrando programa')
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('=-' * 11)
    sleep(1)
print('FIM')
