from mock_data import lista_atracoes

def create_attractions(connection):
  cursor = connection.cursor()

  create_attraction_sql = 'INSERT INTO atracoes (nome, descricao, tipo, horarios) VALUES (?, ?, ?, ?);'

  for atracao in lista_atracoes:
    cursor.execute(create_attraction_sql, (atracao['NOME'], atracao['DESCRICAO'], atracao['TIPO'], atracao['HORARIOS']))

  connection.commit()