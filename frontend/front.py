from flask import Flask, render_template
import requests

app = Flask(__name__)

# URL da API que você deseja conectar
api_url = "http://0.0.0.0:5000"

@app.route('/')
def retorne():
    return 'oi' 

@app.route('/filmes')
def index():
    # Faz uma solicitação GET para a API
    response = requests.get(api_url)

    return response
    # if response.status_code == 200:
    #     data = response.json()
    #     filmes = data.get('filmes', [])
    #     return render_template('index.html', filmes=filmes)
    # else:
    #     return "Erro ao obter os dados da API."

if __name__ == '__main__':
    app.run()
