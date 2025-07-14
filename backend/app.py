from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = 'estoque.json'

# Garante que o arquivo existe
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/listar-itens', methods=['GET'])
def listar_itens():
    with open(DATA_FILE, 'r') as f:
        itens = json.load(f)
    return jsonify(itens)

@app.route('/adicionar-item', methods=['POST'])
def adicionar_item():
    item = request.get_json()

    with open(DATA_FILE, 'r') as f:
        itens = json.load(f)

    itens.append(item)

    with open(DATA_FILE, 'w') as f:
        json.dump(itens, f, indent=2)

    return jsonify({'mensagem': 'Item adicionado com sucesso'}), 201

if __name__ == '__main__':
    app.run(debug=True)
