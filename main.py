from fastapi import FastAPI, Query 
import requests

app = FastAPI()

@app.get('/api/hello')
def bye_planet():
    return {'hello': 'world'}

@app.get('/api/restaurante')
def procurar_restaurantes(restaurante: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        lista_restaurantes = []
        if restaurante is None:
            return {'Dados': dados_json}

        for item in dados_json:
            if item['Company'] == restaurante:
                lista_restaurantes.append({
                "Item" : item['Item'],
                "Preco": item['price'],
                "Descricao" : item['description']
            })
        return{'Restaurante':restaurante, 'Cardápio':lista_restaurantes }
    else:
        return {f'o código do erro: {response.status_code}'}