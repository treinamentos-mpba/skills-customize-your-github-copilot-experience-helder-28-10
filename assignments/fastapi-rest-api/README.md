# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST com FastAPI para cadastrar e consultar tarefas. Pratique rotas HTTP, modelos de dados, parâmetros de caminho, respostas JSON e códigos de status.

## 📝 Tarefas

### 🛠️ Explorar o endpoint de status

#### Descrição
Execute o código inicial e verifique como uma aplicação FastAPI declara uma rota e responde a uma requisição HTTP.

#### Requisitos
O programa concluído deve:

- Iniciar a aplicação FastAPI definida em `starter-code.py` na porta `8000`.
- Disponibilizar `GET /health`, retornando o JSON `{"status": "ok"}`.
- Expor a documentação interativa em `/docs`.

### 🛠️ Listar e cadastrar tarefas

#### Descrição
Use os modelos Pydantic e a lista em memória do código inicial para implementar a listagem e o cadastro de tarefas.

#### Requisitos
O programa concluído deve:

- Retornar todas as tarefas armazenadas ao receber `GET /tasks`.
- Aceitar em `POST /tasks` um JSON com `title` e, opcionalmente, `completed`.
- Atribuir um ID único crescente a cada tarefa criada e mantê-la na lista em memória.
- Responder ao cadastro com status HTTP `201 Created` e os dados da tarefa criada.

Exemplo de corpo da requisição:

```json
{
  "title": "Estudar FastAPI",
  "completed": false
}
```

### 🛠️ Buscar uma tarefa pelo ID

#### Descrição
Implemente uma rota que use um parâmetro de caminho para localizar uma tarefa específica e retorne um erro apropriado quando ela não existir.

#### Requisitos
O programa concluído deve:

- Retornar a tarefa correspondente ao receber `GET /tasks/{task_id}`.
- Responder com status HTTP `404 Not Found` quando não houver tarefa com o ID solicitado.
- Retornar os dados da tarefa em JSON quando ela for encontrada.

Para executar a atividade, instale as dependências com `python -m pip install fastapi uvicorn` e inicie o servidor com `python starter-code.py`. A API ficará disponível em `http://127.0.0.1:8000`.