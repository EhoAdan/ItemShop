from tela_contas import TelaConta
from contas import Contas
from jogador import Jogador
from loja import Loja
from tela_jogador import TelaJogador



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
    
    def pesquisa_emails(self, email_inserido):
        for email_registrado in self.__contas.jogadores:
            if email_registrado.email == email_inserido:
                #Temos um erro aqui. Ele retorna o e-mail inserido, e não o Jogador ao qual ele pertence
                return email_registrado
        return None
    
    def registrar(self):
        while True:
            # Caso não surja o NameError, ou seja, ter o email certo, quebra o loop
            try:
                #Funciona
                email = str(input("Digite seu endereço de e-mail: "))
                if any(email_usado.email == email for email_usado in self.__contas.jogadores):
                    print("E-mail já está em uso")
                    raise NameError
                if ("@" not in email or email[0] == "@" or email[-1] == "@"):
                    raise NameError
                break
            except NameError:
                print("Favor inserir um e-mail válido")
        while True:
            try:
                #Funciona
                nome = str(input("Digite seu nome de usuário: "))
                if any(usuario_existe.nome == nome for usuario_existe in self.__contas.jogadores):
                    print("Nome de usuário já existe")
                    raise NameError
                break
            except NameError:
                print("Favor inserir um nome válido")
        while True:
            try:
                #Funciona
                senha = input("""Digite sua senha
Ela deve possuir:
Ao menos 8 caracteres
Ao menos um número
Ao menos uma letra
""")
                if len(senha) < 8:
                    print("Senha muito curta!")
                    raise NameError
                if not any(caractere.isnumeric() for caractere in senha):
                    print("Senha não possui número!")
                    raise NameError
                if not any(caractere.isalpha() for caractere in senha):
                    print("Senha não possui letra!")
                    raise NameError
                break
            except NameError:
                print("Favor inserir uma senha válida")
        jogador_novo = nome #Dessa forma evitamos de ter um item jogador_novo sendo modificado na lista toda vez que tentamos criar outro
        jogador_novo = Jogador(nome, email, senha)
        self.__contas.jogadores.append(jogador_novo)
        print(f"""Nova conta criada com sucesso!
Seu nome de Jogador é: {nome}
Seu e-mail é: {email}
Sua senha é: {senha}
""")

    def login(self):
        while True:
            try:
                email_inserido = input("Insira seu email: ")
                achou_email_inserido = self.pesquisa_emails(email_inserido)
                if not achou_email_inserido:
                    print("Usuário não encontrado.")
                    raise DadoErradoError
                senha = input("Insira sua senha: ")
                if senha != achou_email_inserido.senha:
                    print("Senha incorreta.")
                    raise DadoErradoError
                return self.jogador_acoes()
            except DadoErradoError:
                pass
        # Gabriel: Não sei bem o que retornar no login por enquanto.
        # Adan: Acho que retorna as ações que o usuario teria. Jogar, Loja (comprar, presentear etc), Amigos (adicionar, excluir) etc.

    def jogador_acoes(self):
        acao = {0: self.__controlador_jogador.fechar_jogo,
                1: self.__controlador_jogador.jogar_partida,
                2: self.__controlador_jogador.abrir_loja,
                3: self.__controlador_jogador.gerenciar_amigos,
                4: self.__controlador_jogador.excluir_conta}
        while True:
            acao[self.__tela_jogador.jogador_opcoes()]()
