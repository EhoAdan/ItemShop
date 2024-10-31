from tela_contas import TelaConta
from contas import Contas
from jogador import Jogador


class ControladorContas:

    def __init__(self, contas):
        # Talvez não precise importar a classe Contas, não tenho certeza
        self.__contas = contas
        self.__tela_conta = TelaConta()
    
    @property
    def contas(self):
        return self.__contas
    
    @property
    def tela_conta(self):
        return self.__tela_conta
    
    def registrar(self):
        while True:
            # Caso não surja o NameError, ou seja, ter o email certo, quebra o loop
            try:
                email = str(input("Digite seu endereço de e-mail: "))
                if (not any(caractere == "@" for caractere in email) or
                    not email[-3] == ".com" or not email[-6] == ".com.br"):
                    # Idealmente, a gente checaria se tem algo depois do @ e antes do .com, mas não sei como
                    raise NameError
                break
            except NameError:
                print("Favor inserir um e-mail válido")
        while True:
            try:
                nome = str(input("Digite seu nome de usuário: "))
                if nome in self.__conta.jogadores:
                    print("Nome de usuário já existe")
                    raise NameError
                break
            except NameError:
                print("Favor inserir um nome válido")
        while True:
            try:
                senha = input("""Digite sua senha
Ela deve possuir:
Ao menos 8 caracteres
Ao menos um número
Ao menos uma letra
""")
                if len(senha) < 8:
                    print("Senha muito curta!")
                    raise NameError
                if not any(caractere.isnumeric for caractere in senha):
                    print("Senha não possui número!")
                if not any(caractere.isalpha() for caractere in senha):
                    print("Senha não possui letra!")
                break
            except NameError:
                print("Favor inserir uma senha válida")
        jogador_novo = Jogador(nome, email, senha)
        self.__contas.jogadores.append(jogador_novo)

    def login(self, email_ou_usuario, senha):
        pass