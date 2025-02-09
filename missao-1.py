#Missão 1: Restaurando as Regras Escolares 📝 
#O vírus apagou os critérios de aprovação dos alunos!
# Para ajudar o Professor Byte a organizar o sistema, 
# sua tarefa é criar um programa que verifique se um 
# aluno foi aprovado (nota maior ou igual à 5) 
# ou reprovado (nota menor ou igual à 5).

nota = input("Digite a nota do aluno: ")

try:
    nota = float(nota)
    if 5 < nota <= 10:
        print("Aprovado!")
    elif 0 <= nota <= 5: 
        print("Reprovado!")
    else:
        print("Você digitou um valor inválido!")
except ValueError:
    print("Você digitou um valor inválido!")