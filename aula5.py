
lista_animal = ['gato', 'cachorro pequeno',  'cachorro médio']

for x in lista_animal:
    print(x)

print("@@@@@@@@@@@@@@@@")

lista = [1, 2, 3, 4]
lista.append(5)
print(sum(lista))
soma = 0
for x in lista:
    print(x)
    soma += x
print("Valor total da somma de lista é {}".format(soma))

"#####################"

lista = [3, 5, 7, 10, 11]
resultado = []
for x in lista:
    if x % 2 == 1:
        resultado.append(x)
print(resultado)
