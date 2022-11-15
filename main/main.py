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

system('clear')

meu_roteiro = []
roteiro_aleatorio = []
menu = {
    1: 'Roteiros',
    2: 'Meu Roteiro',
    3: 'Roteiro Aleatório',
    0: 'Sair'
}

def menu_principal(not_first_run):
    system('clear')
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
            print("\n\t\t LOGIN\n",
                "Operações:\n",
                "1 - Criar Conta\n",
                "2 - Já possuo Conta\n",
                "3 - Esqueci meus dados de Login")

            login_opcao = int(input("\nInsira a operação desejada: "))

            if login_opcao == 1:
                criar_conta(contas, connection)

            elif login_opcao == 2:
                contas = select_users(connection)
                logado = acesso_conta(contas)

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
            
def menu_roteiros():
    system('clear')
    while True:
        print("\nROTEIROS\n")
        for roteiro in roteiros:
            print(roteiro["ID"], "-", roteiro["NOME"])
        print("0 - Voltar")
        opcao = int(input('\nDigite sua opção: '))
        for roteiro in roteiros:
            if opcao == roteiro['ID']:
                system('clear')
                print(f"\n{roteiro['NOME']}\n")
                for n, atracao in enumerate(roteiro['ATRACOES']):
                    print(n+1, atracao['NOME'])
                    print("\t",atracao['DESCRICAO'],"\n")
            elif opcao == 0:
                system('clear')
                menu_principal(True)

def menu_meu_roteiro():
    system('clear')
    while True:
        opcao = int(input('\nMEU ROTEIRO\n\n'
                            '1 - Ver meu roteiro\n'
                            '2 - Mostrar atrações disponíveis\n'
                            '0 - Voltar\n'
                        '\nDigite sua opção: '))
        if opcao == 1:
            if len(meu_roteiro)==0:
                print()
                menu_meu_roteiro()
            else:
                print("\nRoteiro: \n")
                for n, atracao in enumerate(meu_roteiro):
                    print(n+1,atracao['NOME'])
                    print("\t",atracao['DESCRICAO'],"\n")
        elif opcao== 2:
            system('clear')
            print("\nAtrações\n")
            for atracao in atracoes:
                print(atracao["ID"], "-", atracao["NOME"])
            print("0 - Voltar")
            opcao = int(input('\nDigite sua opção: '))
            system('clear')
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
                        system('clear')
                    else:
                        menu_meu_roteiro()
        elif opcao==0:
            menu_principal(True)
        else:
            menu_meu_roteiro()

def role_aleatorio():
    system('clear')
    time.sleep(1)
    print(".\n")
    time.sleep(1)
    print(".\n")
    time.sleep(1)
    print(".\n")
    num_atracoes_alea=random.randint(1,len(atracoes))
    roteiro_aleatorio = random.sample(atracoes,k=num_atracoes_alea)
    print("Roteiro Aleatório\n")
    for n, atracao in enumerate(roteiro_aleatorio):
        print(n+1,atracao['NOME'])
        print("\t",atracao['DESCRICAO'],"\n")

menu_principal(False)