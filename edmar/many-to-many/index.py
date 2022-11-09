import sqlite3
from mock_data import lista_atracoes

connection = sqlite3.connect('./edmar/many-to-many/many-to-many.db')

with open('./edmar/many-to-many/schema.sql') as f:
  connection.executescript(f.read())

cursor = connection.cursor()

# for atracao in lista_atracoes:
#   cursor.execute('INSERT INTO atracoes (nome, descricao, tipo, horarios) VALUES (?, ?, ?, ?);', (atracao['NOME'], atracao['DESCRICAO'], atracao['TIPO'], atracao['HORARIOS']))

# cursor.execute('INSERT INTO roteiros (nome) VALUES (?);', ['Roteiro Família'])
# cursor.execute('INSERT INTO roteiros (nome) VALUES (?);', ['Roteiro Noturno'])
# cursor.execute('INSERT INTO roteiros (nome) VALUES (?);', ['Roteiro Praia e Gastronomia'])

# cursor.execute("INSERT INTO atracao_roteiros (roteiro_id, atracao_id) VALUES (?, ?)", (2, 2))
# cursor.execute("INSERT INTO atracao_roteiros (roteiro_id, atracao_id) VALUES (?, ?)", (2, 1))
# cursor.execute("INSERT INTO atracao_roteiros (roteiro_id, atracao_id) VALUES (?, ?)", (1, 4))

# SELECT storename, productname, productcost FROM _stores 
# JOIN _product_store_relationships ON _stores.id = storereference 
# JOIN _products ON _product_store_relationships.productreference = _products.id
# ORDER BY storename, productname
# ;

# cursor.execute('''SELECT r.* FROM roteiros r
#                   JOIN atracao_roteiros ON r.id = atracao_roteiros.roteiro_id
#                   JOIN atracoes ON atracao_roteiros.atracao_id = atracoes.id
# ''')
cursor.execute('''SELECT 
                    roteiros.id, 
                    roteiros.nome, 
                    atracoes.id,
                    atracoes.nome, 
                    atracoes.descricao, 
                    atracoes.tipo, 
                    atracoes.horarios 
                  FROM atracao_roteiros
                  JOIN roteiros ON atracao_roteiros.roteiro_id = roteiros.id
                  JOIN atracoes ON atracao_roteiros.atracao_id = atracoes.id
                  WHERE roteiros.id = 2
''')

rows = cursor.fetchall()

roteiro =  rows[0]

atracoes = []

for row in rows:
  atracao = {
    "ID": row[2],
    "NOME": row[3],
    "DESCRICAO": row[4],
    "TIPO": row[5],
    "HORARIOS": row[6]
  }

  atracoes.append(atracao)

dict = {
  "ID": roteiro[0],
  'NOME': roteiro[1],
  "ATRACOES": atracoes
}

print(dict)

connection.commit()
connection.close()

# create_table_atracoes = '''CREATE TABLE IF NOT EXISTS atracoes (
#                               id INTEGER PRIMARY KEY,
#                               nome TEXT NOT NULL,
#                               descricao text NOT NULL,
#                               tipo text NOT NULL,
#                               horarios text NOT NULL
#                               );'''

# create_table_roteiros = '''CREATE TABLE IF NOT EXISTS roteiros (
#                               id INTEGER PRIMARY KEY,
#                               nome TEXT NOT NULL,
#                               );'''

# create_table_atracoes_roteiros = '''CREATE TABLE item_assignees (
#                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                 atracao_id INTEGER,
#                                 roteiro_id INTEGER,
#                                 FOREIGN KEY(atracao_id) REFERENCES atracao(id),
#                                 FOREIGN KEY(roteiro_id) REFERENCES roteiro(id)
#                                 );'''
                            

# def create_database():
#   sqliteConnection = None
#   try:

#     print('Banco de dados conectado com sucesso.')
#   except sqlite3.Error as e:
#     print(e)

#   cursor = sqliteConnection.cursor()

#   sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS atracoes (
#                               id INTEGER PRIMARY KEY,
#                               nome TEXT NOT NULL,
#                               descricao text NOT NULL,
#                               tipo text NOT NULL,
#                               horarios text NOT NULL
#                               );'''

#   cursor.execute(sqlite_create_table_query)
#   sqliteConnection.commit()
    
#   return sqliteConnection