contas = [{"ID": 123, "Senha": 456, "Cliente": [123, "Ana Alves", "987", "81998765432"]},
    {"ID": 231, "Senha": 456, "Cliente": [231, "Beatriz Ximenes", "879", "81987654321"]},
    {"ID": 312, "Senha": 456, "Cliente": [312, "Bixa Alves", "798", "81976543210"]}]


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
