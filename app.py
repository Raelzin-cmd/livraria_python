from flask import Flask
from controllers import authors

app = Flask(__name__)

# Rota para lista autores       http://localhost:3000/author
app.add_url_rule('/author', view_func=authors.authors)

app.run(port=3000, debug=True)
