from flask import make_response, jsonify, request
from database import books_repository, authors_repository


def books():
    books = books_repository.get_all()
    return make_response(jsonify(books))

def register_book():
    body = request.get_json()
    author = authors_repository.find_author(body['author_id'])
    
    if author == None:
        return make_response({'message': 'Author not found'}, 404)
    
    book = books_repository.register_book(body['title'], body['publisher'], body['year'], body['author_id'])
    return make_response(jsonify(book), 201)