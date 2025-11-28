from flask import make_response, jsonify
from database import books_repository


def books():
    books = books_repository.get_all()
    return make_response(jsonify(books))