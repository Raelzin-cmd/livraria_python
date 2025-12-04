from flask import Flask
from controllers import authors, books

app = Flask(__name__)

# Rota para Listar Autores      http://localhost:3000/author
app.add_url_rule('/author', view_func=authors.authors)
# Rota para Cadastrar Autor     http://localhost:3000/author
app.add_url_rule('/author', methods=['POST'], view_func=authors.register)
# Rota para Buscar Autor        http://localhost:3000/author/id
app.add_url_rule('/author/<int:id>', view_func=authors.find_author)
# Rota para Editar Autor        http://localhost:3000/author/id
app.add_url_rule('/author/<int:id>', methods=['PUT'], view_func=authors.edit_author)
# Rota para Excluir Autor       http://localhost:3000/author/id
app.add_url_rule('/author/<int:id>', methods=['DELETE'], view_func=authors.delete_author)


# Rota para Listar Livros       http://localhost:3000/books
app.add_url_rule('/book', view_func=books.books)
# Rota para Cadastrar Livros     http://localhost:3000/books
app.add_url_rule('/book', methods=['POST'], view_func=books.register_book)

app.run(port=3000, debug=True)
