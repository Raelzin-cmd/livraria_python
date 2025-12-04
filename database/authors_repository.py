from database.connection import cursor, connect

def get_all():
    result = cursor.execute('SELECT * FROM authors')    # Select all register of table
    authors = result.fetchall() # Return all elements selected
    
    list = []
    
    # Run list
    for author in authors:
        list.append({
            'id': author[0],
            'name': author[1]
        })
    return list

def register_author(name):
    result = cursor.execute('INSERT INTO authors (name) VALUES (%s) RETURNING *', (name,)) # Prevent SQL Injection
    connect.commit()
    author = result.fetchone()
    return {
            'id': author[0],
            'name': author[1]
        }


def find_author(id):
    result = cursor.execute('SELECT * FROM authors WHERE id = %s', (id,))
    author = result.fetchone()
    
    if author == None:
        return None
    
    return {
            'id': author[0],
            'name': author[1]
        }


def edit_author(id, name):
    cursor.execute('UPDATE authors SET name = %s WHERE id = %s', (name, id))
    connect.commit()
    return True


def delete_author(id):
    cursor.execute('DELETE FROM authors WHERE id = %s', (id,))
    connect.commit()
    return True