import random
lancamentos = []
for _ in range(50):
    lancamentos.append(random.randint(1,6))
conta_seis = lancamentos.count(6)
percentual = (conta_seis / 50) * 100
print(f"O valor 6 apareceu {conta_seis} vezes.")
print(f"Percentual de ocorrências da face 6: {percentual}%.")    