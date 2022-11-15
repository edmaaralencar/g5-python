import  time

def menu():
    print("""\tMENU\nRoteiro personalizado\n
Filtros:
1 - Horário do Passeio
2 - Tipo do Passeio
3 - Explorar Passeios
0 - Voltar
""")

def fil_horarios():
    print("""Horário dos Passeios:
1 - Manhã
2 - Tarde
3 - Noite
0 - Voltar
""")
    horario.append(input("Insira os horários desejados [1] [2] ou [3]: ").split())

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
2 - Cultural
3 - Família
4 - Lazer
0 - Voltar
    """)
    tipo.append(input("Insira os tipos desejados [1] [2] [3] ou [4]: ").split())
    filtroTipoAtt[0] = tipo
    return filtroTipoAtt

def explorar():
    print("Explore os Passeios ofertados:")
    # puxar do db todas as atrações disponíveis

def add():
    print("Explore os Passeios ofertados:")
    # puxar do db todas as atrações disponíveis

    cont = 1
    
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
horario = []
tipo = []
ids = []
filtroHorarioAtt = [0]
filtroTipoAtt = [0]

while filtro != 0:
    menu()
    filtro = int(input("Insira o filtro que deseja aplicar: "))
    if filtro == 1:
        fil_horarios()
        if salvar() == 2:
            break
    elif filtro == 2:
        fil_tipos()
        if salvar() == 2:
            break
    elif filtro == 3:
        explorar()
        adicionar = int(input("""Deseja adicionar algum passeio ao seu roteiro?
1 - Sim
2 - Não
    """))
        if adicionar == 1:
            add()
            print(ids)
        elif adicionar == 2:
            salvar()
            if salvar() == 2:
                break
    elif filtro == 0:
        break
    else:
        print("\nComonado não disponível. Favor insira [1] [2] [3] ou [0].\n")
        time.sleep(1)
        print(".\n")

# falta integrar esses filters com o db