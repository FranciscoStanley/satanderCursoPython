class Calculadora:

    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b


    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b


#instaciando a classe

calculadora = Calculadora()
print(calculadora.soma(10, 5))
print(calculadora.subtracao(15, 8))