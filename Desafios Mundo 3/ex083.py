print("{:=^80}".format("Exercícios Python 83"))
print("Crie um programa  onde o usuário digite uma expressâo matematica  qualquer  que use parêntese.")
print("O seu programa deve validar se ela está com quantidade certa de parêntese abertos e fechados ")
print("-="*30)

exp=str(input(f"Digite sua expressão:"))

abertos=exp.count("(")
fechados = exp.count(")")
if abertos == fechados:
    print(f"A sua expressão é válida")
else:
    print(f"Algo está incorreto na quantidade de parêntese,temos {abertos} abertos e {fechados} fechados")

