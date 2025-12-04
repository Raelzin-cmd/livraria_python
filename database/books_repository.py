from database.connection import cursor

def get_all():
    result = cursor.execute('SELECT * FROM books')    # Selecionando todos os registros da tabela
    books = result.fetchall() # Retornando todos os elementos selecionados
    book_list = []   # Lista vazia

    # Percorre toda a lista
    for book in books:
        # Transformando a tupla em dicionário
        book_list.append({
            'id': book[0],
            'title': book[1],
            'publisher': book[2],
            'year': book[3],
            'author': book[4]
        })
    return book_list


def find_author_books(author_id):
    result = cursor.execute('SELECT * FROM books WHERE author_id = %s', (author_id,))
    books = result.fetchall()

    book_list = []

    for book in books:
        book_list.append({
            'id': book[0],
            'title': book[1],
            'publisher': book[2],
            'year': book[3],
            'author': book[4]
        })
    return book_list