frase = str(input('Insira um frase aqui: ')).strip().lower()
frase1 = frase.replace(' ', '')
ql = len(frase1)
i = 0
s = ql - 1
for c in range(0, ql):
    if frase1[c] == frase1[s]:
        s -= 1
        i += 1
if i == ql:
    print('Esse frase é um polídromo!')
else:
    print('Não é um polídromo!')

