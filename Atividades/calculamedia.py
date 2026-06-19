def calcula_media(v):
    soma = 0
    for e in v:
        soma += e
    media = soma/len(v)
    return media

a = [1,2,3,4,5]
calcula_media(a)
b = [10,20,30,40]
calcula_media(b)
print(calcula_media(b))
    