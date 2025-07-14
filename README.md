# 🌿 Mini Farm Stock

**Sistema simples de controle de estoque agrícola**.

## 🎯 Objetivo

Criar uma aplicação web funcional que permita:

- Adicionar itens de estoque
- Listar todos os itens cadastrados
- Persistir os dados localmente usando JSON
- Interagir via API REST (com métodos `GET` e `POST`)
- Treinar integração entre frontend e backend

## 🧰 Tecnologias Utilizadas

| Camada         | Ferramenta / Linguagem        |
|----------------|-------------------------------|
| Frontend       | HTML, CSS, JavaScript         |
| Backend        | Python 3.12, Flask, Flask-CORS|
| Armazenamento  | JSON (`estoque.json`)         |
| Controle de versão | Git + GitHub             |

## 📡 API - Endpoints

### `GET /listar-itens`

- Lista todos os itens cadastrados
- Retorna um JSON com a estrutura:

```json
[
  {
    "nome": "Arroz",
    "quantidade": 50,
    "categoria": "Grão"
  }
]
```

### `POST /adicionar-item`

- Adiciona um novo item ao estoque
- Corpo da requisição (JSON):

```json
{
  "nome": "Milho",
  "quantidade": 20,
  "categoria": "Grão"
}
```

- Resposta:

```json
{ "mensagem": "Item adicionado com sucesso" }
```

## ⚙️ Como rodar o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/by-ester-lima/mini-farm-stock.git
cd mini-farm-stock
```

### 2. Instalar as dependências do backend

```bash
cd backend
pip install -r requirements.txt
```

### 3. Rodar o servidor Flask

```bash
python app.py
```

A API estará disponível em `http://127.0.0.1:5000`

### 4. Executar o frontend

- Abra o arquivo `frontend/index.html` com Live Server no VS Code
- Ou clique duas vezes para abrir no navegador
- O frontend se comunica com o backend via `fetch()` usando os métodos `GET` e `POST`

## 📁 Estrutura do Projeto

```
mini-farm-stock/
├── backend/
│   ├── app.py
│   ├── estoque.json
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
└── README.md
```

## 💡 Diferenciais Técnicos

- Comunicação entre camadas com `fetch` e API REST
- Suporte a CORS para rodar frontend e backend localmente em portas distintas
- Separação clara de responsabilidades entre backend e frontend
- Uso de JSON para armazenamento local
- Código limpo e de fácil leitura

---

✅ Criado por **Ester Lima**
