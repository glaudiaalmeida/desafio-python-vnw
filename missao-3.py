#Missão 3: Recuperando o Sistema de Notas 📊
#As classificações das provas desapareceram!
# Agora os alunos não sabem se tiraram um não 
# sabem se tiraram um A, B, C, D ou F . Antes 
# que o pânico se espalhe, sua tarefa é criar 
# um programa que peça a nota do aluno e imprima
# sua classificação conforme a escala:
#- A (90-100) – "Parabéns, você tirou A!"
#- B (80-89) – "Muito bem, você tirou B."
#- C (70-79) – "Bom trabalho, você tirou C."
#- D (60-69) – "Fique atento, você tirou D."
#- F (menos de 60) – "Estude um pouco mais, você tirou F."


nota = input("Digite a nota do aluno: ")

try:
    nota = int(nota)
    if 90 <= nota <= 100:
        print("Parabéns, você tirou A!")
    elif 80 <= nota <= 89: 
        print("Muito bem, você tirou B.")
    elif 70 <= nota <= 79:
        print("Bom trabalho, você tirou C.")
    elif 60 <= nota <= 69:
        print("Fique atento, você tirou D.")
    elif 0 <= nota <= 59:
        print("Estude um puco mais, você tirou F.")
    else:
      print("Por favor, informe uma nota válida!") 
except ValueError:
    print("Por favor, informe uma nota válida!")
    