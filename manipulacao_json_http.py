import requests
import json
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dicionario_restaurantes = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not     in dicionario_restaurantes:
            dicionario_restaurantes[nome_restaurante] = []

        dicionario_restaurantes[nome_restaurante].append({
            "Item" : item['Item'],
            "Preco": item['price'],
            "Descricao" : item['description']
        })
else:
    print(f'o código do erro: {response.status_code}')


for nome_restaurante, dados in dicionario_restaurantes.items():
    nome_arquivo=f'{nome_restaurante}.json'
    with open (nome_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent = 4)