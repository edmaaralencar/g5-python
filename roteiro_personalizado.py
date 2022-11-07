from database import create_connection, create_database

def select_attractions(connection):
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM atracoes')

    rows = cursor.fetchall()

    atracoes = []
    tupla_nomes = ('id', 'nome', 'descricao', 'tipo', 'horarios')

    for row in rows:
      atracoes.append((dict(zip(tupla_nomes, row))))

    return atracoes

def filter_list_type(arr, type):
  return list(filter(lambda tag: tag['tipo'] == type, arr))

def filter_list_time(arr, times):
  return list(filter(lambda tag: times in tag['horarios'], arr))

def main():
  connection = create_connection()

  with connection:
    create_database(connection)
    atracoes = select_attractions(connection)

    horarios = input("Escreve os horários de preferência (caso necessiten de mais de um horário, coloque entre vírgula: manhã,tarde): ")
    tipo = input("Escreva o tipo do destino (restaurante, histórico, praia): ")

    atracoes_filtradas_por_horarios = filter_list_time(atracoes, horarios)
    atracoes_filtradas = filter_list_type(atracoes_filtradas_por_horarios, tipo)
    print(atracoes_filtradas)
    
  print("\nConexão com banco de dados encerrada.")
  connection.close()

main()