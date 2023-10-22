print('')
print('Desenvolva uma lógica que leia o peso e a altura de uma pessoa, \n calcule seu Índice de Massa Corporal (IMC) e mostre seu status, \n de acordo com a tabela abaixo:')
print('{:=^60}'.format(' TABELA DE PESO IDEAL '))
print('- IMC abaixo de 18,5: Abaixo do Peso')
print('- Entre 18,5 e 25: Peso Ideal')
print('- 25 até 30: Sobrepeso')
print('- 30 até 40: Obesidade')
print('- Acima de 40: Obesidade Mórbida')
print('')

peso = float(input('Informe o seu peso em KG: >>>'))
altura = float(input('Informe a sua altura metros >>>.'))


imc = peso /(altura **2)
print('O IMC desta pessoa é de {:.2f}'.format(imc))

if imc <= 18.5:
    print('Cuidado o seu peso não está ideal para você')
elif 18.5 <= imc <= 25:
    print('Parabéns o seu peso está ideal para você')
elif 25 <= imc <= 30:
    print('Cuidado o seu peso não está ideal para você')
    print('Você está na faixa do SOBREPESO')
elif 30 <= imc <= 40:
    print('Cuidado o seu peso não está ideal para você')
    print('Você está na faixa da OBESIDADE')
elif imc > 40.1:
    print('Cuidado o seu peso não está ideal para você')
    print('Você estána faixa da OBESIDADE MÓRBIDA')
else:
    print('Algo deu errado')
print('')