

lista_numeros = [1, 10]



try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()

    divisao = 10 / 0
    num = lista_numeros[3]

    print("Fechando o arquivo")
    arquivo.close()

except ZeroDivisionError:
    print("Não é possivel divisão por 0")
except ArithmeticError:
    print("Houve um erro ao realizar uma operação aritmética")
except IndexError:
    print("ERRO DESCONHECIDO")
except BaseException as ex:
    print("Erro desconhecido. erro: {}".format(ex))
else:
    print("Executa quando não ocorre exceção")
finally:
    print("Sempre executa")
    print("Fechando arquivo")
    arquivo.close()