import sqlite3
import uuid
from tabulate import tabulate

def create_connection():
    sqliteConnection = None
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        print('Banco de dados conectado com sucesso.')
    except sqlite3.Error as e:
        print(e)
    
    return sqliteConnection

def create_database(connection):
    cursor = connection.cursor()
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS atracoes (
                                id TEXT PRIMARY KEY,
                                nome TEXT NOT NULL,
                                descricao text NOT NULL,
                                tipo text NOT NULL,
                                horarios text NOT NULL
                                );'''

    cursor.execute(sqlite_create_table_query)
    connection.commit()

def create_attraction(connection):
    cursor = connection.cursor()

    nome = input("Digite o nome da atração: ")
    descricao = input("Digite a descrição da atração: ")
    tipo = input("Digite os tipos da atração: ")
    horarios = input("Digite os horários da atração: ")

    create_attraction_sql = 'INSERT INTO atracoes (id, nome, descricao, tipo, horarios) VALUES (?, ?, ?, ?, ?);'

    cursor.execute(create_attraction_sql, (str(uuid.uuid4()), nome, descricao, tipo, horarios))

    connection.commit()

def select_attractions(connection):
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM atracoes')

    rows = cursor.fetchall()

    print("\n")
    print(tabulate(rows, headers=['ID', 'Nome', 'Descricao', 'Tipo', 'Horarios']))

def main():
    connection = create_connection()

    with connection:
        create_database(connection)
        criar_atracao = input("Você deseja criar uma atração? [S] ou [N]: ").upper()

        if criar_atracao == 'S':
            create_attraction(connection)
            
        select_attractions(connection)

    print("\nConexão com banco de dados encerrada.")
    connection.close()

main()

