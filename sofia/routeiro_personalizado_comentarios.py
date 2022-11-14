from database import create_connection, create_database #Importa as funções do codigo database

def select_attractions(connection): #Função que le e traz todos os dados do banco de dados
    cursor = connection.cursor()  #Cursor permite ler e manipular redistros do banco de dados

    cursor.execute('SELECT * FROM atracoes') #Seleciona todos os dados da tabela atrações

    rows = cursor.fetchall() #Guarda todos os dados selecionados na variavel rows

    atracoes = [] #Cria uma lista vazia da atrações
    tupla_nomes = ('id', 'nome', 'descricao', 'tipo', 'horarios') #Cria uma tupla, com o que seram as chaves dos dicionarios

    for row in rows:
      atracoes.append((dict(zip(tupla_nomes, row))))#Adiciona a lista atracoes um dicionario para cada atração, onde as chaves são os dados de tuplas_nomes e os dados as colunas sa tabela atracoes

    return atracoes #Retorna a lista de atracoes fora da função

def filter_list_type(arr, type): #Função que filtra os tipos de atrações
  return list(filter(lambda tag: tag['tipo'] == type, arr)) #Ler a chave tipo no dicionario de cada atração e retorna so aquelas que tem um tipo especifico

def filter_list_time(arr, times): #Função que filtra os horarios de atrações
  return list(filter(lambda tag: times in tag['horarios'], arr)) #Ler a chave horario no dicionario de cada atração e retorna so aquelas que tem um horario especifico

def main(): #Função que conecta todas a funções e faz o sistema funcionar
  connection = create_connection() #Estabelece conecçao com banco SQLite_python

  with connection: #Com a conecção
    create_database(connection) #Cria um banco de atrações, caso não exista
    atracoes = select_attractions(connection) #Guarda todos os dados do banco, dentro da variavel atacoes

    horarios = input("Escreve os horários de preferência (caso necessiten de mais de um horário, coloque entre vírgula: manhã,tarde): ") #Recebe os horarios que o cliente deseja 
    tipo = input("Escreva o tipo do destino (restaurante, histórico, praia): ") #Recebe os tipos de atrações que o cliente deseja

    atracoes_filtradas_por_horarios = filter_list_time(atracoes, horarios) #Filta e retorna somente as atrações do horario escolhido
    atracoes_filtradas = filter_list_type(atracoes_filtradas_por_horarios, tipo) #Filta e retorna somente as atrações do tipo escolhido, entre as atrações já filtradas por horario
    print(atracoes_filtradas) #Exibe as atrações depois de filtratas
    
  print("\nConexão com banco de dados encerrada.")
  connection.close()

main() #Execulta comandos das funções