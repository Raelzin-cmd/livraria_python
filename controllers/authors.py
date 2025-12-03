from flask import make_response, jsonify, request
from database import authors_repository


def authors():
    authors = authors_repository.get_all()
    return make_response(jsonify(authors))


def register():
    body = request.get_json()
    author = authors_repository.register_author(body['name'])
    return make_response(jsonify(author), 201)


def find_author(id):
    author = authors_repository.find_author(id)
    
    if author == None:
        return make_response({'message': 'Author not found'}, 404)

    return make_response(jsonify(author))


def edit_author(id):
    body = request.get_json()
    
    author = authors_repository.find_author(id)
    
    if author == None:
        return make_response({'message': 'Author not found'}, 404)

    authors_repository.edit_author(id, body['name'])
    return make_response({}, 204)