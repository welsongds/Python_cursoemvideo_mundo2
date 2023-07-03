sexo = str(input('Qual o seu sexo de nascimento (F/M): ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Tente novamente, qual seu sexo de nascimento (F/M): ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
