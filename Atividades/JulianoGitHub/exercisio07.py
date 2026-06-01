pares = []
impares = []

while len(pares) + len(impares) < 10:
    num = int(input(f"Digite o {len(pares) + len(impares) + 1}º número inteiro: "))
    
    if num in pares or num in impares:
        print("Erro: Este número já foi inserido. Digite um valor diferente.")
    else:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

print("\nLista de Pares:", pares)
print("Lista de Ímpares:", impares)