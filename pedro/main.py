import random
import time
from os import system

from auth_functions import acesso_conta, criar_conta, select_users
from mock_data import roteiros
from sql_functions import connect_to_database, get_attractions
from credits_functions import siit, credit

connection = connect_to_database()
atracoes = get_attractions(connection)
contas = []

system('cls')

meu_roteiro = []
meus_roteiros = []

roteiro_aleatorio = []
menu = {
    1: 'Roteiros',
    2: 'Roteiro Personalizado',
    3: 'Roteiro Aleatório',
    0: 'Sair'
}
#MENU PRINCIPAL
def menu_principal(not_first_run):
    system('cls')
    siit()

    contas = select_users(connection)

    logado = False
    firstRun = True

    if not_first_run:
        firstRun = False
        logado = True
    else:
        firstRun = True

    if firstRun == True:
        while logado == False:
            print("\nLOGIN\n",
                "1 - Entrar\n",
                "2 - Criar nova conta\n",
                "3 - Esqueci minha senha ou ID" ##  DEAD END, CADÊ CODIGO?
                "\n 0 - Sair")
            login_opcao = int(input("\nDigite sua opção: "))

            if login_opcao == 2:
                criar_conta(contas, connection)

            elif login_opcao == 1:
                contas = select_users(connection)
                logado = acesso_conta(contas)
            elif login_opcao == 0:
                credit()
                exit()
    print('\n')

    while logado == True:
        for key in menu.keys():
            print (key, '-', menu[key])
        opcao = int(input('\nDigite sua opção: '))
        if opcao == 0:
            credit()
            break
        elif opcao == 1:
            menu_roteiros()
        elif opcao == 2:
            menu_meu_roteiro()
        elif opcao == 3:
            role_aleatorio()
        else:
            print("\nOpcão inválida")

# ROTEIROS PRONTOS
def menu_roteiros():
    system('cls')
    while True:
        print("\nROTEIROS\n")
        for roteiro in roteiros:
            print(roteiro["ID"], "-", roteiro["NOME"])
        print("0 - Voltar")
        opcao = int(input('\nDigite sua opção: '))
        for roteiro in roteiros:
            if opcao == roteiro['ID']:
                system('cls')
                print(f"\n{roteiro['NOME']}\n")
                for atracao in roteiro['ATRACOES']:
                    print(atracao['NOME'])
                    print("\t",atracao['DESCRICAO'],"\n")
                print("1 - Exportar Roteiro\n"
                      "0 - Voltar\n")
                print_roteiro = int(input("Digite sua opção: "))
                if print_roteiro == 1: #EXPORTA TXT DO ROTEIRO
                    export = open(f"{roteiro['NOME']}.txt","a", encoding="utf8")
                    for atracao in roteiro['ATRACOES']:
                        export.write(f"{atracao['NOME']}\n")
                        export.write(f"\t {atracao['DESCRICAO']} \n")
                    export.close()
                    system('cls')
                    menu_roteiros()
                elif print_roteiro ==0:
                    system('cls')
                    menu_roteiros()
            elif opcao == 0:
                system('cls')
                menu_principal(True)

#ROTEIRO PERSONALIZADOS
def menu_meu_roteiro():
    system('cls')
    while True:
        opcao = int(input('\nMEUS ROTEIROS\n\n'
                            '1 - Buscar passeios\n'
                            '2 - Ver meu roteiro\n'
                            '3 - Ver roteiros salvos\n'
                            '0 - Voltar\n'
                            '\nDigite sua opção: '))
        #1 - BUSCAR PASSEIOS
        if opcao== 1:
            buscar_passeios()
        #2 - VER MEU ROTEIRO
        elif opcao == 2:
            system('cls')
            if len(meu_roteiro)==0:
                print("\n Não há atrações adicionadas ao seu roteiro")
                time.sleep(1)
                print(".\n")
                time.sleep(1)
                print(".\n")
                menu_meu_roteiro()
            else:
                for atracao in meu_roteiro:
                    print("\n", atracao['NOME'])
                    print("\t",atracao['DESCRICAO'],"\n")

                print("1 - Salvar e exportar meu roteiro\n" # SALVA O ROTEIRO NO BANCO DE DADOS E LIMPAR O meu_roteiro
                      "2 - Apagar Roteiro\n" #NAO CONSEGUI AINDA
                      "0 - Voltar\n")
                save_roteiro = int(input("Digite sua opção: "))
                #1 - SALVAR E EXPORTAR ROTEIRO
                if save_roteiro == 1:
                    id=0
                    for roteiro in meus_roteiros:
                        if roteiro['ID']>id:
                                id=roteiro['ID']
                    nome = input("Digite o nome do seu roteiro: ")
                    meus_roteiros_dict = {"ID": id+1 ,
                                          "NOME": nome,
                                          "ATRACOES": meu_roteiro
                                          }
                    meus_roteiros.append(meus_roteiros_dict)
                    export = open(f"{meus_roteiros_dict['NOME']}.txt","a", encoding="utf8")
                    for atracao in meu_roteiro:
                        export.write(f"{atracao['NOME']}\n")
                        export.write(f"\t {atracao['DESCRICAO']} \n")
                    export.close()
                    system('cls')
                    # NAO CONSIGO LIMPA O  'meu_roteiro' SEM QUEBRAR A CORRENTE
                #2 APAGAR ROTEIRO
                elif save_roteiro == 2:
                    # NAO CONSIGO LIMPA O  'meu_roteiro' SEM QUEBRAR A CORRENTE
                    menu_meu_roteiro()
                elif save_roteiro ==0:
                    menu_meu_roteiro()
        #VER ROTEIROS SALVOS
        elif opcao == 3:
            if len(meus_roteiros)==0:
                print("\nNão há roteiros salvos")
                time.sleep(1)
                print(".\n")
                time.sleep(1)
                print(".\n")
                menu_meu_roteiro()
            else:
                system('cls')
                while True:
                    print("\nMEUS ROTEIROS\n")
                    for roteiro in meus_roteiros:
                        print(roteiro["ID"], "-", roteiro["NOME"])
                    print("\n0 - Voltar")
                    opcao = int(input('\nDigite sua opção: '))
                    for roteiro in meus_roteiros:
                        if opcao == roteiro['ID']:
                            system('cls')
                            print(f"\n{roteiro['NOME']}\n")
                            for atracao in roteiro['ATRACOES']:
                                print(atracao['NOME'])
                                print("\t",atracao['DESCRICAO'],"\n")
                            del_roteiro=int(input("1 - Exportar roteiro\n"
                                                  "2 - Apagar roteiro\n"
                                                  "0 - Voltar\n"
                                                  "\nDigite sua opção: "))

                            #EXPORTAR ROTEIRO
                            if del_roteiro == 1:
                                export = open(f"{roteiro['NOME']}.txt","a", encoding="utf8")
                                for atracao in roteiro['ATRACOES']:
                                    export.write(f"{atracao['NOME']}\n")
                                    export.write(f"\t {atracao['DESCRICAO']} \n")
                                export.close()
                            #APAGAR ROTEIRO
                            elif del_roteiro == 2:
                                roteiro.clear() # PRECISA CORRIGIR COM DB
                                print(meus_roteiros)
                                #system('cls')
                                #menu_meu_roteiro()
                            else:
                                menu_meu_roteiro()
                        elif opcao == 0:
                            system('cls')
                            menu_meu_roteiro()
        #4 - VOLTAR
        elif opcao==0:
            system('cls')
            menu_principal(True)

def role_aleatorio():
    system('cls')
    time.sleep(1)
    print(".\n")
    time.sleep(1)
    print(".\n")
    time.sleep(1)
    print(".\n")
    num_atracoes_alea=random.randint(2,4)
    roteiro_aleatorio = random.sample(atracoes,k=num_atracoes_alea)
    print("Roteiro Aleatório\n")
    for n, atracao in enumerate(roteiro_aleatorio):
        print(n+1,atracao['NOME'])
        print("\t",atracao['DESCRICAO'],"\n")

def buscar_passeios():
    system('cls')
    while True:
        print("\nFILTROS\n"
                "1 - Por horário\n"
                "2 - Por tipo\n"
                "3 - Todos os passeios\n"
                "0 - Voltar\n")
        opcao_filtro= int(input("\nDigite sua opção: "))
        if opcao_filtro==0:
            menu_meu_roteiro()
        elif opcao_filtro==3:
            for atracao in atracoes:
                print(atracao["ID"], "-", atracao["NOME"])
            print("0 - Voltar")
            opcao = int(input('\nDigite sua opção: '))
            system('cls')
            print()
            for atracao in atracoes:
                if opcao == atracao['ID']:
                    print(atracao['ID'], atracao['NOME'])
                    print("\t",atracao['DESCRICAO'],"\n")
                    save = int(input("1 - Deseja adicionar esta atração ao seu roteiro?\n"
                                    "0 - Voltar.\n"
                                    "\nDigite sua opção: "))
                    if save == 1:
                        meu_roteiro.append(atracao)
                        buscar_passeios()
                    elif save == 0:
                        buscar_passeios()
        elif opcao_filtro==2:
            tipo()

        elif opcao_filtro == 1:
            horario()
           
def horario():
    system('cls')
    print("\nHORÁRIO\n"
        "1 - Dia\n"
        "2 - Noite\n"
        "0 - Voltar")
    opcao = int(input("Digite sua opção: "))
    if opcao==0:
        buscar_passeios()
    if opcao==1:
        system('cls')
        for atracao in atracoes:
            if "dia" in atracao['HORARIOS']:
                    print(atracao["ID"], "-", atracao["NOME"])
        print("0 - Voltar")
        opcao = int(input('\nDigite sua opção: '))
        system('cls')
        for atracao in atracoes:
            if opcao == atracao['ID']:
                print(atracao['ID'], atracao['NOME'])
                print("\t",atracao['DESCRICAO'],"\n")
                save = int(input("\n1 - Deseja adicionar esta atração ao seu roteiro?\n"
                        "0 - Voltar.\n"
                        "\nDigite sua opção: "))
                if save == 1:
                    meu_roteiro.append(atracao)
                    horario()
                elif save == 0:
                    horario() 
    if opcao==2:
        system('cls')
        for atracao in atracoes:
            if "noite" in atracao['HORARIOS']:
                    print(atracao["ID"], "-", atracao["NOME"])
        print("0 - Voltar")
        opcao = int(input('\nDigite sua opção: '))
        system('cls')
        for atracao in atracoes:
            if opcao == atracao['ID']:
                print(atracao['ID'], atracao['NOME'])
                print("\t",atracao['DESCRICAO'],"\n")
                save = int(input("\n1 - Deseja adicionar esta atração ao seu roteiro?\n"
                        "0 - Voltar.\n"
                        "\nDigite sua opção: "))
                if save == 1:
                    meu_roteiro.append(atracao)
                    horario()
                elif save == 0:
                    horario() 
def tipo():
    system('cls')
    print("\nTIPO\n"
            "1 - Praias\n"
            "2 - Alimentação\n"
            "3 - Balada\n"
            "4 - Compras\n"
            "0 - Voltar\n")
    opcao_tipo = int(input("Digite sua opção: "))
    if opcao_tipo==0:
        system('cls')
        buscar_passeios()
    if opcao_tipo == 1:
        system('cls')
        for atracao in atracoes:
            if "praia" in atracao['TIPO']:
                print(atracao["ID"], "-", atracao["NOME"])
        print("0 - Voltar")
        opcao = int(input('\nDigite sua opção: '))
        system('cls')
        for atracao in atracoes:
            if opcao == atracao['ID']:
                print(atracao['ID'], atracao['NOME'])
                print("\t",atracao['DESCRICAO'],"\n")
                save = int(input("1 - Deseja adicionar esta atração ao seu roteiro?\n"
                        "0 - Voltar.\n"
                        "\nDigite sua opção: "))
                if save == 1:
                    meu_roteiro.append(atracao)
                    tipo()
                elif save == 0:
                    tipo()
    elif opcao_tipo == 2:
        system('cls')
        for atracao in atracoes:
            if "alimentação" in atracao['TIPO']:
                print(atracao["ID"], "-", atracao["NOME"])
        print("0 - Voltar")
        opcao = int(input('\nDigite sua opção: '))
        system('cls')
        for atracao in atracoes:
            if opcao == atracao['ID']:
                print(atracao['ID'], atracao['NOME'])
                print("\t",atracao['DESCRICAO'],"\n")
                save = int(input("1 - Deseja adicionar esta atração ao seu roteiro?\n"
                        "0 - Voltar.\n"
                        "\nDigite sua opção: "))
                if save == 1:
                    meu_roteiro.append(atracao)
                    tipo()
                elif save == 0:
                    tipo()                
    elif opcao_tipo == 3:
        system('cls')
        for atracao in atracoes:
            if "balada" in atracao['TIPO']:
                print(atracao["ID"], "-", atracao["NOME"])
        print("0 - Voltar")
        opcao = int(input('\nDigite sua opção: '))
        system('cls')
        for atracao in atracoes:
            if opcao == atracao['ID']:
                print(atracao['ID'], atracao['NOME'])
                print("\t",atracao['DESCRICAO'],"\n")
                save = int(input("1 - Deseja adicionar esta atração ao seu roteiro?\n"
                        "0 - Voltar.\n"
                        "\nDigite sua opção: "))
                if save == 1:
                    meu_roteiro.append(atracao)
                    tipo()
                elif save == 0:
                    tipo()   
    elif opcao_tipo == 4:
        system('cls')
        for atracao in atracoes:
            if "compras" in atracao['TIPO']:
                print(atracao["ID"], "-", atracao["NOME"])
        print("0 - Voltar")
        opcao = int(input('\nDigite sua opção: '))
        system('cls')
        for atracao in atracoes:
            if opcao == atracao['ID']:
                print(atracao['ID'], atracao['NOME'])
                print("\t",atracao['DESCRICAO'],"\n")
                save = int(input("1 - Deseja adicionar esta atração ao seu roteiro?\n"
                        "0 - Voltar.\n"
                        "\nDigite sua opção: "))
                if save == 1:
                    meu_roteiro.append(atracao)
                    tipo()
                elif save == 0:
                    tipo()                 

menu_principal(False)