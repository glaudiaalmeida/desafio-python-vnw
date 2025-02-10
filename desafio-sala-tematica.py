#Desafio Cadastro de Pessoas em uma Lista
#Objetivo:
#Você deve criar um programa em Python que permita ao usuário cadastrar 
# um determinado número de pessoas em uma lista.
#Passos:
#Solicite ao usuário a quantidade de pessoas que deseja cadastrar.
#Use um laço while para garantir que a lista seja preenchida com a quantidade correta de nomes.
#A cada iteração, peça ao usuário para inserir um nome e armazene-o na lista.
#Após finalizar o cadastro, exiba a lista com todos os nomes cadastrados.

cadastro = []

pessoas = int(input("Digite a quantidade de pessoas que deseja cadastrar: "))

while pessoas > 0:
    nome = input("Digite o nome da pessoa: ")
    pessoas -= 1
    cadastro.append(nome)

print(pessoas)
print(cadastro)
