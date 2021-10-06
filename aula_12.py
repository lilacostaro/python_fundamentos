import requests

def retorna_dados_cep():
    cep = str(input('Digite o CEP: '))
    response = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    return dados_cep

def retorna_dados_pokemon():
    pokemon = str(input('Digite o nome de um Pokemon: '))
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    #print(dados_pokemon)
    print(dados_pokemon['sprites']['front_shiny'])
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    #retorna_dados_cep()
    retorna_dados_pokemon()
    #response = retorna_response('https://globallabs.academy/')
    #print(response)
