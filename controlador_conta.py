from tela_conta import TelaConta
from conta import Conta


class ControladorConta:

    def __init__(self):

        while opcao_tela == 1:
            try:
                email = str(input("Digite seu endereço de e-mail: "))
                if email: #Fazer teste de e-mail
                    raise NameError
                return email
            except NameError:
                print("Favor inserir um e-mail válido")
            try:
                nome = str(input("Digite seu nome de usuário: "))
                if nome in conta.jogadores:
                    print("Nome de usuário já existe")
                    raise NameError
                return nome
            except NameError:
                print("Favor inserir um nome válido")
            try:
                senha = str(input("""Digite sua senha
Ela deve possuir
Ao menos 8 caracteres
Ao menos um número
Ao menos uma letra
"""))
                if len(senha) < 8:
                    print("Senha muito curta!")
                    raise NameError
                #elif #teste de número
                    print("Senha não possui número!")
                #elif #teste de letra
                    print("Senha não possui letra!")
                return senha
            except NameError:
                print("Favor inserir uma senha válida")
