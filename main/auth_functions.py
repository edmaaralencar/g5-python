import random
import sqlite3

# def create_connection():
#   sqliteConnection = None
#   try:

#     sqliteConnection = sqlite3.connect('siit-database.db')
#     print('Banco de dados conectado com sucesso.')
#   except sqlite3.Error as e:
#     print(e)
    
#   return sqliteConnection

def create_user(connection, id, senha, user_id, user_nome, user_cpf, user_num):
  cursor = connection.cursor()

  create_user_sql = 'INSERT INTO usuarios (id, senha, user_id, user_nome, user_cpf, user_num) VALUES (?, ?, ?, ?, ?, ?);'

  cursor.execute(create_user_sql, (id, senha, user_id, user_nome, user_cpf, user_num))

  connection.commit()

def select_users(connection):
  cursor = connection.cursor()

  cursor.execute('SELECT * FROM usuarios')

  rows = cursor.fetchall()

  usuarios = []

  for row in rows:
    usuario = {
        "ID": row[0],
        "Senha": row[1],
        "Cliente": [
            row[2],
            row[3],
            row[4],
            row[5]
        ]
    }
    usuarios.append(usuario)

  return usuarios

# connection = create_connection()

# contas = select_users(connection)

def criar_conta(contas, connection):
    cad_cpf = input("Insira seu CPF: ")

    list_cpf = []
    for x in range(len(contas)):         
        list_cpf.append(contas[x]["Cliente"][2])
    
    if cad_cpf in list_cpf:
        print("Cpf já cadastrado.")
    else:
        cad_nome = input("Insira seu nome completo: ")
        cad_num = input("Insira seu número de contato: ")
        cad_senha = input("Insira uma senha de até 6 (seis) caracteres: ")

        novo_id = random.randint(1, 10000)

        list_id = []

        for x in range(len(contas)):
            list_id.append(contas[x]["ID"])
        
        for novo_id in list_id:
            novo_id = random.randint(1, 10000)

        id = novo_id
        senha = cad_senha
        user_id = novo_id
        user_nome = cad_nome.title()
        user_cpf = cad_cpf.replace(".", "").strip()
        user_num = cad_num.replace(".", "").strip()

        create_user(connection, id, senha, user_id, user_nome, user_cpf, user_num)

        print(f"Seu ID de acesso é o {novo_id}, guarde-o, será por ele que acessos futuros serão feitos.")

def acesso_conta(contas):
    acesso_ID = input("Insira seu ID de LogIn: ")
    acesso_Senha = input("Insira sua senha: ")

    veri = []

    veri.append(acesso_ID)
    veri.append(acesso_Senha)

    cont = 0

    for i in range (len(contas)):
        elemento = contas[i]
        if veri[0] == str(elemento["ID"]) and veri[1] == elemento["Senha"]:
            armazen = elemento["Cliente"]
            cont += 1
            break

    if cont == 0:
        print('\nDados incorretos ou não encontrados.\nPor favor insira novamente ou realize novo cadastro.')
        return False
    else:
        print(f"\nSeja bem vindo {armazen[1]}!")      # falta fluxo de como armazenar o acesso
        return True

def recuperar_conta():
    print("Etapa de Verificação.")
    nome = input("Insira seu nome: ")
    cpf = input("Insira seu CPF: ")
    num = input("Insira seu número de contato: ")

    veri = []

    veri.append(nome.title())
    veri.append(cpf.replace(".", "").replace(" ",""))
    veri.append(num.replace(".", "").replace(" ",""))

    cont = 0

    for pessoa in contas:
        cliente = pessoa['Cliente']

        if cont == 0:
            print('Não encontrou ninguém.')
            break

        if cliente[1] == veri[0] and cliente[2] == veri[1] and cliente[3] == veri[2]:
            print(pessoa) 
            cont += 1
            break

def main_autenticacao(contas):
    print("\t\t LOGIN\n",
        "Operações:\n",
        "1 - Criar Conta\n",
        "2 - Já possuo Conta\n",
        "3 - Esqueci meus dados de Login")

    login_opcao = int(input("Insira a operação desejada: "))

    if login_opcao == 1:
        criar_conta(contas)

    elif login_opcao == 2:
        acesso_conta(contas)

    elif login_opcao ==3:
        recuperar_conta()
