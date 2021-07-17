conjunto = {1, 2, 3, 4}
print(conjunto)
conjunto.add(5)
print(conjunto)
conjunto.discard(5)
print(conjunto)

#uniao

conjunto = {1, 2, 3, 4, 5}
conjunto2 ={5, 6, 7, 8, 9}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)

#interseção

conjunto_intersecao = conjunto.intersection(conjunto2)
print(conjunto_intersecao)

#diferença

conjunto_diferenca =  conjunto.difference(conjunto2)
conjunto_diferenca2 =  conjunto2.difference(conjunto)
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)

print(conjunto_diferenca)

print(conjunto_diferenca2)

print(conjunto_dif_simetrica)


conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}

conjunto_subset = conjunto_a.issubset(conjunto_b)
print("-----------------")
print(conjunto_subset)

conjunto_subset = conjunto_b.issubset(conjunto_a)
print("-----------------")
print(conjunto_subset)

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print("-----------------")
print(conjunto_superset)

conjunto_superset = conjunto_a.issuperset(conjunto_b)
print("-----------------")
print(conjunto_superset)
print("-----------------")

#removendo duplicidade

listas = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(listas)
print(conjunto_animais)

