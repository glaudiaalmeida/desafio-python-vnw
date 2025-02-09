#Missão 5: Recuperando o Cofre de Segurança 🔒
#O cofre da biblioteca guarda códigos raros de programação, 
# mas o vírus resetou a senha! Agora, apenas quem souber a 
# combinação correta poderá acessá-lo.
#Crie um programa que solicite ao usuário uma senha e verifique 
# se ela está correta. A senha correta é "Python123".

senha = 'Python123'

while True:
    senha_informada = input("Informe a senha: ")
    
    if senha_informada == senha:
        print("Seu acesso a biblioteca está liberado!")
        break
    else:
        print("Senha incorreta. Tente novamente.")
        
