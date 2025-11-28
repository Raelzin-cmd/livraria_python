from flask import Flask
from controllers import authors

app = Flask(__name__)

# Cria uma rota e importa função
app.add_url_rule('/', view_func=authors.test)

app.run(port=3000, debug=True)