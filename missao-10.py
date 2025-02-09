#Missão 10: Contando Letras 🔄
#O sistema precisa contar quantas letras há em um nome.
#➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
#➡️ Exemplo: contar_letras("Ana")
#➡️ Saída:" O nome Ana tem 3 letras"

def contar_letras(nome):
   total_letras = len(nome)
   return total_letras

nome = input("Digite o nome do aluno: ")

quantidade_letras = contar_letras(nome)

print(f"O nome '{nome}' possui {quantidade_letras} letras")