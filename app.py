from flask import Flask, jsonify
import json
from pathlib import Path
from os.path import join

app = Flask(__name__)

# Caminho do arquivo JSON exportado
json_path = Path(__file__).parent / 'Output' / 'index.json'

# Carregar os dados do JSON
with open(json_path, encoding='utf-8') as f:
    dados = json.load(f)

@app.route('/', methods=['GET'])
def home():
    """Página inicial com informações sobre a API"""
    return "Oi"

@app.route('/imoveis', methods=['GET'])
def get_properties():
    """Retorna a lista de imóveis"""
    return jsonify(dados['list'])

@app.route('/schema', methods=['GET'])
def get_schema():
    """Retorna o schema dos dados (exemplo simplificado)"""
    schema = {
        "id": "string",
        "uf": "string",
        "cidade": "string",
        "bairro": "string",
        "endereco": "string",
        "preco": "string",
        "valor": "string",
        "desconto": "string",
        "descricao": "string",
        "venda": "string",
        "link": "string"
    }
    return jsonify(schema)

if __name__ == '__main__':
    app.run(debug=True)