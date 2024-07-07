print("{:=^80}".format("Exercícios Python 81"))
print("")
print("Faça um programa que leia vários números e coloque em uma lista, depois responda:")
print(" A)-Quantos numeros foram digitados. \n B) -Mostre a lista ordenada de forma decrescente \n C) Se o valor 5 foi digitado verifique se existe ou não na lista")
print("")

lista = []
while True:
    valor = int(input("Digite um valor:"))
    lista.append(valor)
    print(f'Deseja digitar outro número?')
    resp=input(f"S/N: " ).upper()
    if resp == "N":
        break

if 5 in lista:
    x = "Sim ele está na lista"
else:
    x = "Não está na lista"
 
print('-='*30)

print(f'A nossa lista é ', lista)
print(f'A)Foram digitados:',len(lista),'números!')
print(f'B) A lista na ordem reversa é',sorted(lista,reverse=True))
print(f'C)',x)