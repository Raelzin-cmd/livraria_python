from flask import Flask
from controllers import authors, books

app = Flask(__name__)

# Rota para lista autores       http://localhost:3000/author
app.add_url_rule('/author', view_func=authors.authors)
# Rota para lista livros       http://localhost:3000/books
app.add_url_rule('/book', view_func=books.books)
# Rota para cadastrar livros    http://localhost:3000/author
app.add_url_rule('/author', methods=['POST'], view_func=authors.register)
app.add_url_rule('/author/<int:id>', view_func=authors.find_author)


app.run(port=3000, debug=True)
