#criar um arquivo
def escrever_arquivos(texto):
    diretorio = 'D:/santanderCursos/santanderCursoPython/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()
#atulizando arquivo
def atualizar_arquivos(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()
#lendo arquivo
def ler_arquivos(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':

    #escrever_arquivos("\nNome: Francisco Stanley")
    atualizar_arquivos("\nNome: Sabrina de Sousa")
    #ler_arquivos('teste.txt')