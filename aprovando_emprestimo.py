print('Você deseja um emrpréstimo, então vamos preencher as informações:')
sal = float(input('Qual valor do seu salário?  R$'))
valcasa = float(input('Qual o valor do imóvel que você deseja comprar? R$'))
anos = int(input('Enquantos anos você pretende pagar esse valor?'))
valmensal = valcasa / (anos * 12)
sal_30 = sal * 0.3
if valmensal > sal_30:
    print('Infelizmente seu empréstimo foi negado!')
elif valmensal <= sal_30:
    print('Seu empréstimo foi aceito!')
    print('O valor do sua parcela mensal fica R${:.2f}, durante um périodo de {} anos'.format(valmensal, anos))
