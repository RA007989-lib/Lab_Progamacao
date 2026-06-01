nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

nomes_invertidos = nomes[::-1]

print("\nLista original:", nomes)
print("Lista invertida:", nomes_invertidos)