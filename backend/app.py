from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'backend/estoque.json'

# Cria o arquivo estoque.json se não existir
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/api/estoque', methods=['GET'])
def listar_estoque():
    with open(DATA_FILE) as f:
        dados = json.load(f)
    return jsonify(dados)

@app.route('/api/estoque', methods=['POST'])
def adicionar_item():
    novo_item = request.json
    with open(DATA_FILE) as f:
        dados = json.load(f)
    dados.append(novo_item)
    with open(DATA_FILE, 'w') as f:
        json.dump(dados, f, indent=2)
    return jsonify({'mensagem': 'Item adicionado com sucesso'}), 201

if __name__ == '__main__':
    app.run(debug=True)
