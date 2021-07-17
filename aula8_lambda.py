
contador_letras = lambda lista:[len(x) for x in lista]

lista_animais = ['Cachorro', 'Gato', 'Veado']
contador_letras(lista_animais)
print(contador_letras(lista_animais))

print("-------------------------------")

soma = lambda a, b: \
    a + b
subtracao = lambda a, b: \
    a - b
print(soma(20, 5))
print(subtracao(20, 5))

print('-------------------------------')

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b
}

soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
print("Valor da soma de a + b é: {}".format(soma(5, 5)))
print("O valor da subtração de a - b é: {}".format(subtracao(5,4)))
print("O valor da multiplicação de a x b é: {}".format(multiplicacao(5,5)))