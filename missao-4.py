#Missão 4: Restaurando a Identificação de Números ⚖️
#Os robôs da escola precisam identificar padrões numéricos para resolver
# cálculos e otimizar os sistemas. No entanto, o vírus bagunçou os 
# algoritmos e agora eles não conseguem mais somar corretamente!
#Crie um programa que peça dois números ao usuário e exiba a soma deles.

while True:
    try:
        numero_1 = int(input("Digite o primeiro número inteiro: "))
        numero_2 = int(input("Digite o segundo número inteiro: "))
        break
    except ValueError:
        print("Erro! Você deve digitar apenas números inteiros. Tente novamente.")

print(f"A soma dos números informados é: {numero_1 + numero_2}")
    