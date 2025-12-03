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

register_author('Fred Oliveira')