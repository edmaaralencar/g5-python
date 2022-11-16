import sqlite3
import  time

def menu():
    print("""\tMENU\nRoteiro personalizado\n
Filtros:
1 - Horário do Passeio
2 - Tipo do Passeio
3 - Explorar Passeios
4 - Meus Roteiros
0 - Voltar
""")

def fil_horarios():
    print("""Horário dos Passeios:
1 - Dia
2 - Noite
0 - Voltar
""")
    hor = input("Insira os horários desejados [1] ou [2]: ")
    
    trans_dictHorario = {"1": "dia", "2": "noite"}
    transTable_hor = hor.maketrans(trans_dictHorario)
    hor_trans = hor.translate(transTable_hor).split()

    horario.append(hor_trans)

    if len(horario) > 1:
        continuar = int(input("""Já existe filtro definido para esse critério.\n Deseja salvar novo?
1 - Sim
2 - Não
"""))
        if continuar == 2:
            horario.pop()
        
    filtroHorarioAtt[0] = horario[-1]
    return filtroHorarioAtt

def fil_tipos():
    print("""Tipos de Passeio:
1 - Praia
2 - Alimentação
3 - Balada
4 - Compras
0 - Voltar
""")

    tip = input("Insira os tipos desejados [1] [2] [3] ou [4]: ")

    trans_dictTipo = {"1": "praia", "2": "alimentação", "3": "balada", "4": "compras"}
    trans_tableTip = tip.maketrans(trans_dictTipo)
    tip_trans = tip.translate(trans_tableTip).split()

    tipo.append(tip_trans)

    if len(tipo) > 1:
        continuar = int(input("""Já existe filtro definido para esse critério.\n Deseja salvar novo?
1 - Sim
2 - Não
Resposta: """))
        if continuar == 2:
            tipo.pop()

    filtroTipoAtt[0] = tipo[-1]
    return filtroTipoAtt

def explorar():
    print("Explore os Passeios ofertados:")

    conn = sqlite3.connect('main-database.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * from atracoes;
    """)
    print("id\t|\tnome\t|\tdescricao\t|\ttipo\t|\thorarios")
    for linha in cursor.fetchall():
        print(linha)

def add():
    print("Passeios ofertados:")

    conn = sqlite3.connect('main-database.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * from atracoes;
    """)

    cont = 1
    
    while cont != 0:
        print("id\t|\tnome\t|\tdescricao\t|\ttipo\t|\thorarios")
        for linha in cursor.fetchall():
            print(linha)
        
        id = int(input("\nInsira o ID do Passeio que deseja adicionar: "))
        ids.append(id)

        continuar = int(input("""Deseja adicionar algum outro passeio ao seu roteiro?
1 - Sim
2 - Não
Resposta: """))

        if continuar == 1:
            cont = 1
        elif continuar == 2:
            cont = 0

    return ids

def salvar():
    finalizar = int(input("""Deseja adicionar algum outro filtro?
1 - Sim
2 - Não
Resposta: """))
    return finalizar

def int_db():
    conn = sqlite3.connect('main-database.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * from atracoes;
    """)

    roteiro = []

    for linha in cursor.fetchall():
        for i in range(len(ids)):
            if ids[i] == linha[0]:
                print(ids[i])
                comp = (linha in roteiro)
                if comp == False:
                    roteiro.append(linha)
        
        for i in range(len(filtroHorarioAtt)):
            for j in range(len(filtroHorarioAtt[i])):
                if filtroHorarioAtt[i][j] in linha[4]:
                    comp = (linha in roteiro)
                    if comp == False:
                        roteiro.append(linha)
        
        for i in range(len(filtroTipoAtt)):
            for j in range(len(filtroTipoAtt[i])):
                if filtroTipoAtt[i][j] in linha[3]:
                    comp = (linha in roteiro)
                    if comp == False:
                        roteiro.append(linha)
        
    if len(roteiro) == 0:
        print("Ainda não existem passeios com esses critérios. Favor pesquisar com outros filtros.")
        time.sleep(1)
        print(".\n")

    else:
        print(f"Seu Roteiro:\n{roteiro}")
        
        save = input("""Deseja salvar seu roteiro?
1 - Sim
0 - Voltar
Resposta: """)

        if save == "1":     # tem que ser atualizado para formatar a saída
            key = input("Insira o nome de seu roteiro: ")
            meus_roteiros[key] = roteiro

filtro = 1
horario = []
tipo = []
ids = []
filtroHorarioAtt = ["0"]
filtroTipoAtt = ["0"]

meus_roteiros = {}

while filtro != 0:
    menu()
    filtro = int(input("Insira o filtro que deseja aplicar: "))
    if filtro == 1:
        fil_horarios()
        if salvar() == 2:
            int_db()
    elif filtro == 2:
        fil_tipos()
        if salvar() == 2:
            int_db()
    elif filtro == 3:
        explorar()
        adicionar = int(input("""\nDeseja adicionar algum passeio ao seu roteiro?
1 - Sim
2 - Não
Resposta: """))
        if adicionar == 1:
            add()
            if salvar() == 2:
                int_db()
        elif adicionar == 2:
            if salvar() == 2:
                int_db()
    
    elif filtro == 4:
        ### falta ordenar os roteiros
        ## falta o fluxo de exportar
        print(f"Meus Roteiros: {meus_roteiros}")

        escolhido = input("""Qual Roteiro deseja visualizar?""")
        
    elif filtro == 0:
        break
    else:
        print("\nComando não disponível. Favor insira [1] [2] [3] ou [0].\n")
        time.sleep(1)
        print(".\n")
        time.sleep(1)
        print(".\n")