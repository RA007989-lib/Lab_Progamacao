numeros = []

for i in range(6):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

x = int(input("Digite um número para pesquisar (x): "))

quantidade = numeros.count(x)

print(f"\nO número {x} aparece {quantidade} vez(es) na lista.")

if quantidade > 0:
    primeira_posicao = numeros.index(x)
    print(f"A primeira ocorrência está no índice: {primeira_posicao}")