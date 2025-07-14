const form = document.getElementById('estoque-form');
const lista = document.getElementById('lista-estoque');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const nome = document.getElementById('nome').value;
  const quantidade = parseInt(document.getElementById('quantidade').value);
  const categoria = document.getElementById('categoria').value;

  const item = { nome, quantidade, categoria };

  await fetch('http://localhost:5000/api/estoque', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(item)
  });

  form.reset();
  listarEstoque();
});

async function listarEstoque() {
  const res = await fetch('http://localhost:5000/api/estoque');
  const dados = await res.json();

  lista.innerHTML = '';
  dados.forEach(item => {
    const li = document.createElement('li');
    li.textContent = `${item.nome} - ${item.quantidade} (${item.categoria})`;
    lista.appendChild(li);
  });
}

listarEstoque();
