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
            total = valor1 + (valor1 * 7/100)
            print(f'\033[1;30;44m-= O valor total da sua compra é R${total:.2f} com 7% de Juros =- \033[m')
        elif v ==2:
            total = valor1 + (valor1 * 14/100)
            parcela = total/2
            print(f'\033[1;30;44m-= O valor total da sua compra é R${total:.2f} parcelado em 2x de R${parcela:.2f} com 14% de Juros =- \033[m')
        elif v ==3:
            total = valor1 + (valor1 * 21/100)
            parcela = total/3
            print(f'\033[1;30;44m-= O valor total da sua compra é R${total:.2f} parcelado em 3x de R${parcela:.2f} com 21% de Juros =- \033[m')
        else:
            print('Total de parcelas inválidas')
    elif dc == 'D':
        total = valor1 + (valor1 *2/100)
        print('Débito')
        print(f'\033[1;30;44m-= O valor total da sua compra é R${total:.2f}  =-\033[m')
elif fp == 2:
    print('Dinheiro!')
    print(f'O valor da sua compra foi de R${valor1}.')
print('\033[1;30;44m----- Obrigado e volte Sempre! -----\033[m')
