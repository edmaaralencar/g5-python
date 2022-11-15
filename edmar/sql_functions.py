from mock_data import lista_atracoes

def create_attractions(connection):
  cursor = connection.cursor()

  create_attraction_sql = 'INSERT INTO atracoes (nome, descricao, tipo, horarios) VALUES (?, ?, ?, ?);'

  for atracao in lista_atracoes:
    cursor.execute(create_attraction_sql, (atracao['NOME'], atracao['DESCRICAO'], atracao['TIPO'], atracao['HORARIOS']))

  connection.commit()

def create_user(connection, user):
  cursor = connection.cursor()

  create_user_sql = 'INSERT INTO usuarios (nome, descricao, tipo, horarios) VALUES (?, ?, ?, ?);'

  cursor.execute(create_user_sql, (user['NOME'], user['DESCRICAO'], user['TIPO'], user['HORARIOS']))

  connection.commit()

def select_attractions(connection):
  cursor = connection.cursor()

  cursor.execute('SELECT * FROM atracoes')

  rows = cursor.fetchall()

  atracoes = []
  tupla_nomes = ('ID', 'NOME', 'DESCRICAO', 'TIPO', 'HORARIOS')

  for row in rows:
    atracoes.append((dict(zip(tupla_nomes, row))))

  return atracoes

def select_users(connection):
  cursor = connection.cursor()

  cursor.execute('SELECT * FROM usuarios')

  rows = cursor.fetchall()

  atracoes = []
  tupla_nomes = ('ID', 'NOME', 'DESCRICAO', 'TIPO', 'HORARIOS')

  for row in rows:
    atracoes.append((dict(zip(tupla_nomes, row))))

  return atracoes