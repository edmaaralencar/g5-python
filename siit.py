from os import system
import time
import random

system('cls')
atracao1 ={
    'ID':1,
    'NOME':"Restaurante Beiramar",
    'DESCRICAO': "Melhores frutos do mar de Maceió.",
    'TIPO':["alimentação"],
    'HORARIO': "dia"
}
atracao2 ={
    'ID':2,
    'NOME':"Praia do Sol",
    'DESCRICAO': "Bela praia com piscinas naturais e passeios de bugre.",
    'TIPO':["praia"],
    'HORARIO': ["dia"]
}
atracao3 ={
    'ID':3,
    'NOME':"Boate Love",
    'DESCRICAO': "Melhor boate de Maceió.",
    'TIPO':["balada"],
    'HORARIO': ["noite"]
}
atracao4 ={
    'ID':4,
    'NOME':"Feira de Artesanato",
    'DESCRICAO': "Artesanato típico de Alagoas.",
    'TIPO':["compras"],
    'HORARIO': ['noite','dia']}
atracao5 ={
    'ID':5,
    'NOME':"Bar do Jangadeiro",
    'DESCRICAO': "Jovens reunidos, cerveja gelada e ótimos petiscos.",
    'TIPO':["alimentação", "balada"],
    'HORARIO': ['noite']
}

atracoes = [atracao1,atracao2,atracao3,atracao4,atracao5]

roteiro1 = {
    'ID':1,
    'NOME':"Roteiro Família",
    'ATRACOES': [atracao2,atracao1,atracao4]
}
roteiro2 = {
    'ID':2,
    'NOME':"Roteiro Noturno",
    'ATRACOES': [atracao5,atracao3]
}
roteiro3 = {
    'ID':3,
    'NOME':"Roteiro Praia e Gastronomia",
    'ATRACOES': [atracao2,atracao1,atracao5]
}

roteiros=[roteiro1,roteiro2,roteiro3]

meu_roteiro = []
roteiro_aleatorio = []

menu = {
    1: 'Roteiros',
    2: 'Meu Roteiro',
    3: 'Roteiro Aleatório',
    0: 'Sair'
}
def menu_principal():
    system('cls')
    siit()
    while True:
        for key in menu.keys():
            print (key, '-', menu[key])
        opcao = int(input('\nDigite sua opção: '))
        if opcao == 0:
            credit()
            exit()
        elif opcao == 1:
            menu_roteiros()
        elif opcao == 2:
            menu_meu_roteiro()
        elif opcao == 3:
            role_aleatorio()
        else:
            print("\nOpcão inválida")
            
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
                for n, atracao in enumerate(roteiro['ATRACOES']):
                    print(n+1, atracao['NOME'])
                    print("\t",atracao['DESCRICAO'],"\n")
            elif opcao == 0:
                system('cls')
                menu_principal()
def menu_meu_roteiro():
    system('cls')
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
                for n, atracao in enumerate(meu_roteiro):
                    print(n+1,atracao['NOME'])
                    print("\t",atracao['DESCRICAO'],"\n")
        elif opcao== 2:
            system('cls')
            print("\nAtrações\n")
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
                        system('cls')
                    else:
                        menu_meu_roteiro()
        elif opcao==0:
            menu_principal()
        else:
            menu_meu_roteiro()

def role_aleatorio():
    system('cls')
    time.sleep(1)
    print(".\n")
    time.sleep(1)
    print(".\n")
    time.sleep(1)
    print(".\n")
    num_atracoes_alea=random.randint(1,len(atracoes))
    roteiro_aleatorio = random.choices(atracoes,k=num_atracoes_alea)
    print("Roteiro Aleatório\n")
    for n, atracao in enumerate(roteiro_aleatorio):
        print(n+1,atracao['NOME'])
        print("\t",atracao['DESCRICAO'],"\n")

def siit():
    print("""
███████ ██       ██ ████████ 
██      ██       ██    ██    
███████ ██ █████ ██    ██    
     ██ ██       ██    ██    
███████ ██       ██    ██    
 """)
def credit():
    system('cls')
    print("""
       @@@@@@   @@@                   @@@  @@@@@@@  
      @@@@@@@   @@@                   @@@  @@@@@@@  
      !@@       @@!                   @@!    @@!    
      !@!       !@!                   !@!    !@!    
      !!@@!!    !!@     @!@!@!@!@     !!@    @!!    
       !!@!!!   !!!     !!!@!@!!!     !!!    !!!    
           !:!  !!:                   !!:    !!:    
          !:!   :!:                   :!:    :!:    
      :::: ::    ::                    ::     ::    
      :: : :    :                     :       :     
    ╔═╗┌┐┌┌─┐  ╔╗ ┌─┐┌─┐┌┬┐┬─┐┬┌─┐  ╔═╗┬ ┬  ┬┌─┐┌─┐  
    ╠═╣│││├─┤  ╠╩╗├┤ ├─┤ │ ├┬┘│┌─┘  ╠═╣│ └┐┌┘├┤ └─┐  
    ╩ ╩┘└┘┴ ┴  ╚═╝└─┘┴ ┴ ┴ ┴└─┴└─┘  ╩ ╩┴─┘└┘ └─┘└─┘  
    ╔═╗┌┐┌┌─┐  ╔╗ ┌─┐┌─┐┌┬┐┬─┐┬┌─┐  ╦═╗┌─┐┌─┐┬ ┬┌─┐  
    ╠═╣│││├─┤  ╠╩╗├┤ ├─┤ │ ├┬┘│┌─┘  ╠╦╝│ ││  ├─┤├─┤  
    ╩ ╩┘└┘┴ ┴  ╚═╝└─┘┴ ┴ ┴ ┴└─┴└─┘  ╩╚═└─┘└─┘┴ ┴┴ ┴  
        ╔═╗┌─┐┬┌─┐  ╦  ╦┬┬  ┌─┐  ╔╗╔┌─┐┬  ┬┌─┐           
        ║  ├─┤││ │  ╚╗╔╝││  ├─┤  ║║║│ │└┐┌┘├─┤           
        ╚═╝┴ ┴┴└─┘   ╚╝ ┴┴─┘┴ ┴  ╝╚╝└─┘ └┘ ┴ ┴           
     ╔═╗┬  ┌─┐┬─┐┌─┐  ╦ ╦┌─┐┌┐┌┌┬┐┌─┐┬─┐┬  ┌─┐┬ ┬     
     ║  │  ├─┤├┬┘├─┤  ║║║├─┤│││ ││├┤ ├┬┘│  ├┤ └┬┘     
     ╚═╝┴─┘┴ ┴┴└─┴ ┴  ╚╩╝┴ ┴┘└┘─┴┘└─┘┴└─┴─┘└─┘ ┴      
           ╔═╗┌┬┐┌┬┐┌─┐┬─┐  ╦═╗┌─┐┌─┐┬ ┬┌─┐                 
           ║╣  │││││├─┤├┬┘  ╠╦╝│ ││  ├─┤├─┤                 
           ╚═╝─┴┘┴ ┴┴ ┴┴└─  ╩╚═└─┘└─┘┴ ┴┴ ┴                 
    ╔═╗┬ ┬┬┬  ┬ ┬┌─┐┬─┐┌┬┐┌─┐  ╔═╗┬┬ ┬  ┬┌─┐┬┬─┐┌─┐  
    ║ ╦│ │││  ├─┤├┤ ├┬┘│││├┤   ╚═╗││ └┐┌┘├┤ │├┬┘├─┤  
    ╚═╝└─┘┴┴─┘┴ ┴└─┘┴└─┴ ┴└─┘  ╚═╝┴┴─┘└┘ └─┘┴┴└─┴ ┴  
         ╔═╗┌─┐┌┬┐┬─┐┌─┐  ╔═╗┌─┐┌─┐┬  ┬ ┬┌─┐              
         ╠═╝├┤  ││├┬┘│ │  ║  │ │├┤ │  ├─┤│ │              
         ╩  └─┘─┴┘┴└─└─┘  ╚═╝└─┘└─┘┴─┘┴ ┴└─┘              
           ╦═╗┬┌─┐┌─┐┬─┐┌┬┐┌─┐  ╦  ┬┌┬┐┌─┐                  
           ╠╦╝││  ├─┤├┬┘ │││ │  ║  ││││├─┤                  
           ╩╚═┴└─┘┴ ┴┴└──┴┘└─┘  ╩═╝┴┴ ┴┴ ┴                  
     ╔═╗┌─┐┌─┐┬┌─┐  ╦  ╦┌─┐┬  ┌─┐┌┬┐┌─┐┬─┐┌─┐┌─┐      
     ╚═╗│ │├┤ │├─┤  ╚╗╔╝├─┤│  ├─┤ ││├─┤├┬┘├┤ └─┐      
     ╚═╝└─┘└  ┴┴ ┴   ╚╝ ┴ ┴┴─┘┴ ┴─┴┘┴ ┴┴└─└─┘└─┘      
          ╦  ╦┬┬─┐┌┐┌┌─┐  ╔═╗┌┬┐┌─┐┬─┐┌─┐┬                 
          ╚╗╔╝│├┬┘│││├─┤  ╠═╣│││├─┤├┬┘├─┤│                 
           ╚╝ ┴┴└─┘└┘┴ ┴  ╩ ╩┴ ┴┴ ┴┴└─┴ ┴┴─┘               
           
 .d8888b      .d88b.      .d8888b       8888b.      888d888 
d88P"        d8P  Y8b     88K              "88b     888P"   
888          88888888     "Y8888b.     .d888888     888     
Y88b.    d8b Y8b.     d8b      X88 d8b 888  888 d8b 888     
 "Y8888P Y8P  "Y8888  Y8P  88888P' Y8P "Y888888 Y8P 888     
 
                      888                       888 
                      888                       888 
    .d8888b   .d8888b 88888b.   .d88b.  .d88b.  888 
    88K      d88P"    888 "88b d88""88bd88""88b 888 
    "Y8888b. 888      888  888 888  888888  888 888 
         X88 Y88b.    888  888 Y88..88PY88..88P 888 
     88888P'  "Y8888P 888  888  "Y88P"  "Y88P"  888 
 """)
menu_principal()