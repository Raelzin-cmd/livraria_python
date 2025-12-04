from database.connection import cursor, connect

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


def register_book(title, publisher, year, author_id):
    result = cursor.execute('INSERT INTO books (title, publisher, year, author_id) VALUES (%s, %s, %s, %s) RETURNING *', (title, publisher, year, author_id)) # Prevent SQL Injection
    connect.commit()
    book = result.fetchone()
    return {
            'id': book[0],
            'title': book[1],
            'publisher': book[2],
            'year': book[3],
            'author': book[4]
        }


def find_book(id):
    result = cursor.execute('SELECT * FROM books WHERE id = %s', (id,))
    book = result.fetchone()
    
    if book == None:
        return None
    
    return {
            'id': book[0],
            'title': book[1],
            'publisher': book[2],
            'year': book[3],
            'author': book[4]
        }


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


def edit_book(id, title, publisher, year, author_id):
    cursor.execute('UPDATE books SET title = %s, publisher = %s, year = %s, author_id = %s WHERE id = %s', (title, publisher, year, author_id, id))
    connect.commit()
    return True


def delete_book(id):
    cursor.execute('DELETE FROM books WHERE id = %s', (id,))
    connect.commit()
    return True