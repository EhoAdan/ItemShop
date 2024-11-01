from tela_contas import TelaConta
from contas import Contas
from jogador import Jogador

class DadoErradoError(Exception):
    # Provavelmente é bom jogar isso pra outro arquivo mas fica aqui por enquanto
    pass

class ControladorContas:

    def __init__(self, contas = None):
        # Talvez não precise importar a classe Contas, não tenho certeza
        self.__contas = contas
        self.__tela_conta = TelaConta()
    
    @property
    def contas(self):
        return self.__contas
    
    @property
    def tela_conta(self):
        return self.__tela_conta
    
    def pesquisa_nomes(self, usuario):
        for registrado in self.__contas.jogadores:
            if registrado.nome == usuario:
                return usuario
        return None
    
    def registrar(self):
        while True:
            # Caso não surja o NameError, ou seja, ter o email certo, quebra o loop
            try:
                email = str(input("Digite seu endereço de e-mail: "))
                if (not any(caractere == "@" for caractere in email) or
                    not (email[-4:] == ".com" or email[-7:] == ".com.br")):
                    # Idealmente, a gente checaria se tem algo depois do @ e antes do .com, mas não sei como
                    raise NameError
                break
            except NameError:
                print("Favor inserir um e-mail válido")
        while True:
            try:
                nome = str(input("Digite seu nome de usuário: "))
                if any(usuario_existe.nome == nome for usuario_existe in self.__contas.jogadores):
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
                    raise NameError
                if not any(caractere.isalpha() for caractere in senha):
                    print("Senha não possui letra!")
                    raise NameError
                break
            except NameError:
                print("Favor inserir uma senha válida")
        jogador_novo = Jogador(nome, email, senha)
        self.__contas.jogadores.append(jogador_novo)

    def login(self):
        while True:
            try:
                usuario = input("Insira o usuário ou email: ")
                senha = input("""(Requisitos: mais de 8 caracteres, ao menos uma letra e um número)
Insira a senha: """)
                achou_usuario = self.pesquisa_nomes(usuario)
                if not achou_usuario:
                    print("Usuário não encontrado.")
                    raise DadoErradoError
                if senha != achou_usuario.senha:
                    print("Senha incorreta.")
                    raise DadoErradoError
                break
            except DadoErradoError:
                pass
        # Não sei bem o que retornar no login por enquanto
        return True