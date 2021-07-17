import requests

def retorna_dados_cep(cep):

    #Usando api para retorna endereço do cep

    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    #Imprimindo status da requisição
    print(response.status_code)

    #Imprimindo texto do response
    print(response.text)
    #print(response.json())
    #print(type(response.text))
    #print(type(response.json()))
    #dados_cep = response.json()
    #print(dados_cep['logradouro'])
    #print(dados_cep['bairro'])
    return response

#Consumindo api rest full pokemon
def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

if __name__ == '__main__':
    cep_inserido = input("Insira o cep: ")
    retorna_dados_cep(cep_inserido)
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon)

