vetor = []
for i in range(10):
    valor = input(f"Digite o {i+1} valor: ")
    vetor.append(valor)
valores_diferentes = len(set(vetor))
print(f"Existem {valores_diferentes} valores diferentes no vetor.")    
    