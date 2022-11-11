import sqlite3
import uuid
from tabulate import tabulate

def create_connection(): #Função para conectar um banco de dados
    sqliteConnection = None #Definimos essa variavel fora do escopo try expect para podermos acessa-la fora.
    try: #Tentar conectar o banco de dados
        sqliteConnection = sqlite3.connect('SQLite_Python.db') #Comando para conectar banco SQLite_Python.db
        print('Banco de dados conectado com sucesso.')
    except sqlite3.Error as e: #Informar caso de erro ao conctar
        print(e)
    
    return sqliteConnection #Retorna a concção com SQLite

def create_database(connection): #Função para criar o banco de atrações, caso ainda não exista
    cursor = connection.cursor() #Cursor permite ler e manipular redistros do banco de dados
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS atracoes (
                                id TEXT PRIMARY KEY,
                                nome TEXT NOT NULL,
                                descricao text NOT NULL,
                                tipo text NOT NULL,
                                horarios text NOT NULL
                                );'''  #Comandos que vão ser execultados dentro do danco de dados
                                       #CREATE TABLE IF NO EXIXRS = cria uma tabela atracoes no banco, caso ela ainda não exista

    cursor.execute(sqlite_create_table_query) #Execulta comandos de sqlite_create_table_query diretamente no banco de dados
    connection.commit() #Salva todas as alterações feitas no banco desta função

def create_attraction(connection): #Função para criar uma atração nova no banco, na tabela atracoes
    cursor = connection.cursor() #Cursor permite ler e manipular redistros do banco de dados

    #Antes recebe algumas variaveis
    nome = input("Digite o nome da atração: ")
    descricao = input("Digite a descrição da atração: ")
    tipo = input("Digite os tipos da atração: ")
    horarios = input("Digite os horários da atração: ")

    create_attraction_sql = 'INSERT INTO atracoes (id, nome, descricao, tipo, horarios) VALUES (?, ?, ?, ?, ?);' #INSERT INTO = coloque em
                                                                                                                 #VALUES = os valores
    cursor.execute(create_attraction_sql, (str(uuid.uuid4()), nome, descricao, tipo, horarios))#Execulta o comando de create_attraction_sql com os valores da lista

    connection.commit()#Salva as mudanças feitas na tabela atracoes

def select_attractions(connection): #Função para ler os dados de atracoes e exibi-los em uma tabela
    cursor = connection.cursor()#Cursor permite ler e manipular redistros do banco de dados

    cursor.execute('SELECT * FROM atracoes')#Seleciona todos os dados da tabela atracoes

    rows = cursor.fetchall()#???

    print("\n")
    print(tabulate(rows, headers=['ID', 'Nome', 'Descricao', 'Tipo', 'Horarios']))#Exibe uma tabela com os dados de atracoes

def main():#????
    connection = create_connection()#Estabelece variavel connection que conecta o banco de dados

    with connection:#Com a conecção
        create_database(connection)#Cria um banco de atrações
        criar_atracao = input("Você deseja criar uma atração? [S] ou [N]: ").upper()#Questiona se o usuario deseja criar uma nova atração, resposta sempre vai sair em maiusculo por conta do comando upper

        if criar_atracao == 'S':#Caso a resposta do usuario seja S
            create_attraction(connection)#Cria uma nova atração com os dados oferecidos pelo usuario
            
        select_attractions(connection)#Exibe uma tabela com todas as atrações

    print("\nConexão com banco de dados encerrada.")
    connection.close()#Fecha a conecção com o banco de dados

main()#???
