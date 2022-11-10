import random

def criar_conta():

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
        
        cliente = []
        cliente.append(novo_id)
        cliente.append(cad_nome.title())
        cliente.append(cad_cpf.replace(".", "").strip())
        cliente.append(cad_num.replace(".", "").strip())

        novo_cad = {"ID": 0, "Senha": 0, "Cliente": cliente}

        novo_cad["ID"] = novo_id
        novo_cad["Senha"] = cad_senha

        contas.append(novo_cad)
        contas_att = []
        contas_att = contas

        print(f"Seu ID de acesso é o {novo_id}, guarde-o, será por ele que acessos futuros serão feitos.")

def acesso_conta():
    acesso_ID = input("Insira seu ID de LogIn:\n")
    acesso_Senha = input("Insira sua senha:\n")

    veri = []

    veri.append(acesso_ID)
    veri.append(acesso_Senha)

    cont = 0

    for i in range (len(contas)):
        elemento = contas[i]
        if veri[0] == elemento["ID"] and veri[1] == elemento["Senha"]:
            armazen = elemento["Cliente"]
            cont += 1
            break

    if cont == 0:
        print('Dados incorretos ou não encontrados.\nPor favor insira novamente ou realize novo cadastro.')
    else:
        print(f"Seja bem vindo {armazen[1]}!")      # falta fluxo de como armazenar o acesso

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

def main():
    print("\t\t LOGIN\n",
        "Operações:\n",
        "1 - Criar Conta\n",
        "2 - Já possuo Conta\n",
        "3 - Esqueci meus dados de Login")

    login_1 = int(input("Insira a operação desejada: "))

    if login_1 == 1:
        criar_conta()

    elif login_1 == 2:
        acesso_conta()

    elif login_1 ==3:
        recuperar_conta()

main()