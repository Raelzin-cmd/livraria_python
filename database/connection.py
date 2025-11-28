import os   # Importando variáveis de ambiente
from dotenv import load_dotenv  # Importando a conexão das variáveis
import psycopg  # Realizar a conexão com o banco de dados

load_dotenv()   # Inicializando a conexão das variáveis de ambiente

# Transformando em variáveis locais
user = os.getenv('db_user') 
pwd = os.getenv('db_pass')

connection = psycopg.connect(
    f'postgresql://{user}:{pwd}@localhost/library'
)

# Testando a conexão
cursor = connection.cursor()

allBooks = cursor.execute('SELECT * FROM books')    # Selecionando todos os registros da tabela

print(allBooks.fetchall())   # Trazendo todos os registros76