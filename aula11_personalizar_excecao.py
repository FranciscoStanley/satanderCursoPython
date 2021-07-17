#Criando class error para fazer o tratamento de erro
class Error(Exception):
    pass

#Criando class InputError para fazer tratamento de erros de entrada de nota para não passar de 10.
class InputError(Error):
    #Criando um construtor
    def __init__(self, massage):
        self.massage = massage

while True:

    try:
        x = int(input("Entre com a nota de 0 a 10: "))
        print("Valor digitado: {}".format(x))
        if x > 10:
            #forçando uma exceção com comando raise recebendo InputError
            raise InputError("Nota não pode ser maior que 10!")
        elif x < 0:
            raise InputError("Nota não pode ser menor que 0 por exemplo: -1, -2...")
        break

    except ValueError:
        print("Não pode usar letras neste campo, apenas números!")
    except InputError as ex:
        print(ex)