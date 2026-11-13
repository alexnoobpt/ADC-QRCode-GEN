import json
import os

File="contas.json"
if os.path.exists(File):
    with open(File, "r") as f:
        contas=json.load(f)
else:
    contas={} #por enquanto é um dicionario msm

def menu():
  
    print(r"""
         _____            __      __              
        / ____|           | |     | |              
        | |     __ _ _ __ | |_ ___| |__   __ _ ___ 
        | |    / _` | '_ \| __/ __| '_ \ / _` / __|
        | |___| (_| | |_) | || (__| | | | (_| \__ \
         \_____\__,_| .__/ \__\___|_| |_|\__,_|___/
                    | |                            
                    |_| Maker""") 
    
    print("")                   
    print("ESCOLHA 1 - Iniciar Sessão")
    print("ESCOLHA 2 - Criar Conta")  
    opcao=input("Escolha uma opção: ") 
    return opcao

def validar_palavra_passe(password):   
    while len(password)!=6:
            password=input("Palavra-passe deve ter 6 caracteres, tente novamente, por favor!")
    return password

def iniciar_sessao():
    print("Inicie a sessão!")
    utilizador=input("Nome do Utilizador: ")
    password=validar_palavra_passe(input("Palavra-passe: "))
    if utilizador in contas and contas[utilizador]==password:
        print("Sessão iniciado com sucesso!")
    else:
        print("Erro, por favor, tente novamente!")

def criar_conta():
    print("Crie uma nova conta!")
    utilizador=input("Escolha o nome de um utilizador: ")
    if utilizador in contas:
        print("Erro este utilizador já existe, por favor, tente novamente!")
        return
    password=validar_palavra_passe(input("Crie uma palavra-passe de 6-caracteres:"))
    contas[utilizador]=password
    with open(File, "w") as f:
        json.dump(contas, f)
    print("Conta criada com sucesso!")
    
def main():
    opcao=menu()
    if opcao=="1":
        iniciar_sessao()
    elif opcao=="2":
        criar_conta()
    else:
        print("Erro, por favor, tente novamente!")
        

if __name__ == "__main__":
    main()
