#Missão 2: O Sistema Eleitoral Secreto 📝 
#O grêmio estudantil da escola realiza votações
# para decidir melhorias e inovações, mas o vírus 
# desativou a verificação de elegibilidade para votar!
# Sua tarefa é criar um programa que pergunte a idade 
# do usuário e informe se ele pode votar (mínimo: 16 anos).

idade = input("Digite sua idade: ")

try:
    idade = int(idade)
    if 0 < idade < 16:
        print("Você não tem idade mínima para participar!")
    elif 16 <= idade <= 100:
        print("Pode se dirigir a mesa de votação!")
    else:
        print("Por favor, digite uma idade válida!")
except ValueError:
    print("Por favor, digite uma idade válida!")
    