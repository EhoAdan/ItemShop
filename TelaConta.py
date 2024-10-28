from conta import Conta


class TelaConta():
    def TelaConta(self):
        print("""-------- TelaInicial ---------
Escolha sua opção:
1- Criar nova conta
2- Log in
0- Sair do sistema
""")

        while True:
            try:
                opcao_usuario = int(input("Escolha uma opção: "))
                if not -1 < opcao_usuario < 3:
                    """Caso o usuário faça algo além de inserir 1, 2, 3 ou 0, já joga um valueerror logo,
                    já que é o que já tem a resposta de erro"""
                    raise ValueError
                return opcao_usuario
            except ValueError:
                print("Favor inserir uma opção válida.")
        
        while opcao_usuario == 1:
            try:
                e-mail = str(input("Digite seu endereço de e-mail: "))
                if e-mail: #Fazer teste de e-mail
                    raise NameError
                return e-mail
            except NameError:
                print("Favor inserir um e-mail válido")
            try:
                nome = str(input("Digite seu nome de usuário: "))
                if nome in jogadores:
                    print("Nome de usuário já existe")
                    raise NameError
                if palavrao in nome:
                    #Fazer teste de nome. Acho que podemos fazer uma função pra isso, com uma lista e tals
                    print("Por favor, não use palavras ofensivas")
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
