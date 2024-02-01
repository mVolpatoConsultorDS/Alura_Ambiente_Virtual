from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    
    End point que exibe uma mensagem incrivel do mundo da programacao

    '''
    return {'Hello':'Word'}

#tostart the apiserver:
#uvicorn main:app --reload

#consultar un cardapio
#http://127.0.0.1:8000/api/restaurantes/?restaurante=McDonald%E2%80%99s

#http://127.0.0.1:8000/docs

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    End point que retorna os items de cardapio dos restaurantes
    

    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json}

        #print(dados_json)
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({'item': item['Item'], "price": item['price'], 'description': item['description']})
        return {'Restaurante':restaurante, 'Cardapio':dados_restaurante}
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}