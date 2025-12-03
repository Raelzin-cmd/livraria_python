from flask import make_response, jsonify, request
from database import authors_repository


def authors():
    authors = authors_repository.get_all()
    return make_response(jsonify(authors))

def register():
    body = request.get_json()
    author = authors_repository.register_author(body['name'])
    return make_response(jsonify(author), 201)