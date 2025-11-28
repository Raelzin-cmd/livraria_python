from flask import make_response, jsonify
from database import authors_repository


def authors():
    authors = authors_repository.get_all()
    return make_response(jsonify(authors))