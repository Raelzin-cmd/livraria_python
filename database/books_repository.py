from database.connection import cursor

def get_all():
    result = cursor.execute('SELECT * FROM books')    # Selecionando todos os registros da tabela
    books = result.fetchall() # Retornando todos os elementos selecionados
    list = []   # Lista vazia
    # Percorre toda a lista
    for book in books:
        # Transformando a tupla em dicionário
        list.append({
            'id': book[0],
            'title': book[1],
            'publisher': book[2],
            'year': book[3],
            'author': book[4]
        })
    return list