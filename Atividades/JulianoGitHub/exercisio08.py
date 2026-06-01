frase = input("Digite uma frase curta: ")

palavras = []
palavra_atual = ""

for caractere in frase:
    if caractere != " ":
        palavra_atual += caractere
    else:
        if palavra_atual != "":
            palavras.append(palavra_atual)
            palavra_atual = ""

if palavra_atual != "":
    palavras.append(palavra_atual)

print("Vetor de palavras:", palavras)