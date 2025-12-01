Instale o dotenv para usar variáveis de ambiente
 ```bash
python -m pip install python-dotenv
 ```

Inicializando o container docker

```bash
docker compose up -d

services:
  postgres:
    container_name: livraria_bancodedados
    image: postgres:16-alpine
    environment:
      POSTGRES_PASSWORD: password
      POSTGRES_USER: user
    volumes:
      - ./data/postgres:/var/lib/postgresql/data
    ports:
      - port:port
```


Beekeeper:

```sql
CREATE DATABASE livraria;

-- GESTÃO DA LIVRARIA (id, name)
CREATE TABLE authors(
  -- Gera ID automáticamente
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

-- TABELA DE LIVROS (id, title, publisher, year, author_id(id))
CREATE TABLE books(
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  publisher TEXT NOT NULL,
  year INT NOT NULL,
  author_id INT NOT NULL,
  -- ID do livro fará referência ao ID do autor
  FOREIGN KEY (author_id) REFERENCES authors(id)
);

```

Biblioteca: psycopg

[psycopg documentation]("https://www.psycopg.org/psycopg3/docs/basic/install.html")

```bash
python -m pip install "psycopg[binary]"
```

Após fazer o connection.py

Preencha um dado no banco de dados para testar a aplicação