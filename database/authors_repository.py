from database.connection import cursor, con

def get_all():
    result = cursor.execute('SELECT * FROM authors')    # Selecionando todos os registros da tabela
    authors = result.fetchall() # Retornando todos os elementos selecionados
    list = []   # Lista vazia
    # Percorre toda a lista
    for author in authors:
        # Transformando a tupla em dicionário
        list.append({
            'id': author[0],
            'name': author[1]
        })
    return list

def register_author(name):
    result = cursor.execute('INSERT INTO authors (name) VALUES (%s)', (name,)) # Previnindo SQL Injection
    con.commit()
    return result

register_author('Lauren Kate')