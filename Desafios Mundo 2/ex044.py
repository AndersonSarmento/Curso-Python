print()
print('Elabore um programa que calcule o valor a ser pago por um produto, \n considerando o seu preço normal e condição de pagamento:')
print('{:=^60}'.format(' LOJAS GUANABARA '))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque: 10% de desconto')
print('[2] à vista no cartão: 5% de desconto')
print('[3] 2x no cartão: preço formal')
print('[4] 3x ou mais no cartão: 20% de juros')
print('___________________________________________________________ \n')
valor = float(input('Insira o valor do seu produto R$ '))
print('[1] À vista')
print('[2] Parcelado')
opcao1 = int(input('À vista ou parcelado?'))



a =  valor * 0.10
b =  valor * 0.05 
c =  (valor/2)
juros = (valor*0.20)
d =  (valor + juros)


if opcao1 == 1:
    print('{:=^60}'.format(' LOJAS GUANABARA '))
    print('[a] No dinheiro ou cheque 10% de desconto')
    print('[b] No cartão 5% de desconto')
    opcao2 = input('Qual sua opção: ')
    if opcao2 == 'a':
        print('{:=^60}'.format(' Sua opção foi à vista no DINHEIRO '))
        print('Valor da sua compra: R${}'.format(valor))
        print('Desconto aplicado:   R${}'.format(a))
        print('Valor pagamento:     R$',(valor-a))
        print('{:=^60}'.format(' Obrigado!'))    
    elif opcao2== 'b':
        print('{:=^60}'.format(' Sua opção foi à vista no CARTÃO '))
        print('Valor da sua compra: R${}'.format(valor))
        print('Desconto aplicado:   R${}'.format(b))
        print('Valor para pagamento R$',(valor-b))
        print('{:=^60}'.format(' Obrigado!'))
    else:
        print('Quando de errado não está certo aqui')
elif opcao1 == 2:
    print('{:=^60}'.format(' LOJAS GUANABARA '))
    print('[c] No cartão em 2x preço normal')
    print('[d] No cartão em 3x com 20% de juros')
    opcao3 = input('Qual sua opção: ')
    if opcao3 == 'c':
        print('{:=^60}'.format(' No cartão em 2x preço NORMAL '))
        print('Valor da sua compra: R${}'.format(valor))
        print('Valor da parcela 1/2 R${}'.format(c))
        print('{:=^60}'.format(' Obrigado!'))    
    elif opcao3 == 'd':
        print('{:=^60}'.format(' No cartão em 3x com 20% de JUROS '))
        parcelas = int(input('Quantas vezes: '))
        print('Valor da sua compra: R${}'.format(valor))
        print('Valor dos Juros R${}'.format(juros))
        print('Valor da parcela', (d)/parcelas)
        print('Valor final de pagamento R$',(d))
        print('{:=^60}'.format(' Obrigado!'))
    else:
        print('Quando de errado não está certo aqui')
else:
    print('Quando de errado não está certo')
print('')