def menu():
    print("""\tMENU\nRoteiro personalizado\n
Filtros:
1 - Horário do Passeio
2 - Tipo do Passeio
3 - Explorar Passeios
0 - Voltar
""")

    filtro = int(input("Insira o filtro que deseja aplicar: "))
    return filtro

def fil_horarios():
    print("""Horário dos Passeios:
1 - Manhã
2 - Tarde
3 - Noite
0 - Voltar
""")
    horario = []
    horario = input("Insira os horários desejados [1] [2] ou [3]: ").split()
    filtroHorarioAtt[0] = horario
    return filtroHorarioAtt

def fil_tipos():
    print("""Tipos de Passeio:
1 - Praia
2 - Cultural
3 - Família
4 - Lazer
0 - Voltar
    """)

    tipo = []
    tipo = input("Insira os tipos desejados [1] [2] [3] ou [4]: ").split()
    filtroTipoAtt[0] = tipo
    return filtroTipoAtt

def explorar():
    print("Explore os Passeios ofertados:")
    # puxar do db todas as atrações disponíveis

    adicionar = int(input(""""Deseja adicionar algum passeio ao seu roteiro?
1 - Sim
2 - Não
    """))

    return adicionar

def add():
    print("Explore os Passeios ofertados:")
    # puxar do db todas as atrações disponíveis

    cont = 1
    ids = []
    
    while cont != 0:
        id = int(input("Insira o ID do Passeio que deseja adicionar: "))
        ids.append(id)

        continuar = int(input(""""Deseja adicionar algum outro passeio ao seu roteiro?
    1 - Sim
    2 - Não
        """))

        if continuar == 1:
            cont = 1
        elif continuar == 2:
            cont = 0

    return ids

def salvar():
    finalizar = int(input("""Deseja adicionar algum outro filtro?
1 - Sim
2 - Não
    """))
    return finalizar

filtro = 1
filtroHorarioAtt = [0]
filtroTipoAtt = [0]

while filtro != 0:
    menu()
    if filtro == 1:
        fil_horarios()
        print(filtroHorarioAtt)
        salvar()
    elif filtro == 2:
        fil_tipos()
        print(filtroTipoAtt)
        salvar()
    elif filtro == 3:
        explorar()
        if adicionar == 1:
            add()
        elif adicionar == 2:
            salvar()
    elif filtro == 0:
        break
    else:
        print("Favor insira [1] [2] [3] ou [0].")
