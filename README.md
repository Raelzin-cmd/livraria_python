# 📚 livraria_python

Um projeto de CRUD para gerenciamento de **autores** e **livros**, desenvolvido em **Python** com **Flask**, **PostgreSQL** e **Docker**. O sistema permite cadastrar, listar, buscar, atualizar e remover autores e livros.

---

## 🚀 Descrição do Projeto

Este projeto implementa uma API simples de uma livraria. O fluxo de dados funciona da seguinte forma:

* Autores são cadastrados informando apenas o **nome**, e o **ID** é gerado automaticamente pelo PostgreSQL.
* Livros são cadastrados com **título**, **publicado**, **ano** e o **id do autor**, permitindo a relação entre livros e seus respectivos autores.

A API foi testada utilizando o **Postman** e o banco gerenciado via **Beekeeper Studio**.

---

## 🛠 Tecnologias Utilizadas

* **Python**
* **Flask**
* **psycopg[binary]** (conexão com PostgreSQL)
* **PostgreSQL**
* **Docker** (imagem: `postgres:16-alpine`)
* **dotenv** (variáveis de ambiente)
* **Beekeeper Studio** (gerenciamento do banco)

---

## 📦 Instalação e Requisitos

Antes de iniciar, certifique-se de ter instalado:

* Python 3.10+
* Docker e Docker Compose
* Beekeeper Studio (ou outro cliente SQL de sua preferência)

### Dependências utilizadas

No ambiente virtual local (`.venv`), são instaladas:

* Flask
* psycopg[binary]
* python-dotenv

---

## ▶️ Como Rodar o Projeto

### 1. Subir o container do PostgreSQL

```bash
docker-compose up -d
```

### 2. Ativar o ambiente virtual

```bash
source .venv/Scripts/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz com:

```
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
PORT=5432
```

### 5. Conectar ao banco pelo Beekeeper

Use as variáveis acima para acessar o banco e executar as **queries de criação das tabelas**.

#### 📌 Onde encontrar o SQL?

```
database/schema.sql
```

---

## 📚 Funcionalidades

* Cadastro de autores
* Listagem de autores
* Busca de autor por ID
* Atualização de autor
* Exclusão de autor
* Cadastro de livros
* Listagem de livros
* Buscar livro por ID
* Atualização de livro
* Exclusão de livro

---

## 📁 Estrutura de Pastas

```
livraria_python/
│  app.py
│  docker-compose.yml
│  .env
│  .data/
│  .venv/
│  .gitignore
│
├── controllers/
│     ├── __init__.py
│     ├── authors.py
│     └── books.py
│
└── database/
        ├── __init__.py
        ├── authors_repository.py
        ├── books_repository.py
        ├── connection.py
        └── schema.sql
```

---

## 👨‍💻 Autor

**Israel Almeida - Contato**

* GitHub: [https://github.com/Raelzin-cmd](https://github.com/Raelzin-cmd)
* LinkedIn: [https://www.linkedin.com/in/israel-almeida-d29n1198](https://www.linkedin.com/in/israel-almeida-d29n1198)
* Telefone: **(61) 98272-1088**