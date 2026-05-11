vetor = []
for i in range(5):
    vetor.append(input(f"Digite o valor da posição {i}: "))
x = input("Digite o valor X para buscar: ")
if x in vetor:
    posicao = vetor.index(x)
    print(f"O valor apareceu primeiro na posição: {posicao}")
else:
    print("-1")        