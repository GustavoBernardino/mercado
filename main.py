print('\033[1;30;44m<----Ola Bem vindo ao Super Mercado Gubs---->\033[m')
print('\033[34mColoque o produto e o valor abaixo!')
cont = valor1 = 0
while True:
    produto = str(input('Produto: '))
    valor = float(input('Valor: R$'))
    cont += 1
    valor1 += valor
    qc =' '
    while qc not in 'SN':
        qc = str(input('Quer continuar? [S/N]')).upper()
    if qc == 'N':
        break
fp = int(input('\033[34mDigite a forma de pagamento ,1 Cartão ou 2 Dinheiro: '))
if fp == 1:
    dc = str(input('Débito ou Crédito? [D/C]')).upper()

if dc == 'C':
    print('Crédito!')
    v = int(input('Gostaria de parcelas em quantas vezes? [1/2/3] '))
    if v ==1:
        print('\033[1;30;44m-= O valor total da sua compra é R${:.2f} com 7% de Juros =- \033[m'.format(valor1 + (valor1 * 7/100)))
    elif v ==2:
        print('\033[1;30;44m-= O valor total da sua compra é R${:.2f} parcelado em 2x de R${:.2f} com 21% de Juros =- \033[m'.format(valor1 + (valor1 * 14 / 100),(valor+(valor * 14/100))/2))
    elif v ==3:
        print('\033[1;30;44m-= O valor total da sua compra é R${:.2f} parcelado em 3x de R${:.2f} com 21% de Juros =- \033[m'.format(valor1 + (valor1 * 21 / 100),(valor+(valor * 21/100))/3))
if dc == 'D':
    print('Débito')
    print('\033[1;30;44m-= O valor total da sua compra é R${:.2f}  =-\033[m'.format(valor1 + (valor1 *2/100)))
if fp == 2:
    print('Dinheiro!')
    print(f'O valor da sua compra foi de R${valor1}.')
print('\033[1;30;44m----- Obrigado e volte Sempre! -----\033[m')
