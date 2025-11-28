from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')

def test():
    return make_response('Tudo certo')

app.run(port=3000, debug=True)