from personagem import Personagem


class Jogador:
    
    def __init__(self, nome: str, email: str, senha: str, saldo: int = 0, dinheiro_gasto: int = 0, presentes_dados: int = 0, presentes_recebidos: int = 0, partidas_jogadas: int = 0):
        # acho que a gente faz essa checagem de tipos na hora de criar a conta
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__saldo = saldo
        self.__dinheiro_gasto = dinheiro_gasto
        self.__presentes_dados = presentes_dados
        self.__presentes_recebidos = presentes_recebidos
        self.__partidas_jogadas = partidas_jogadas
        self.__amigos = []
        self.__personagens = []
        self.__skins = []
        self.__chromas = []
        self.__historico_compras = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def dinheiro_gasto(self):
        return self.__dinheiro_gasto

    @dinheiro_gasto.setter
    def dinheiro_gasto(self, dinheiro_gasto):
        self.__dinheiro_gasto = dinheiro_gasto

    @property
    def presentes_dados(self):
        return self.__presentes_dados

    @presentes_dados.setter
    def presentes_dados(self, presentes_dados):
        self.__presentes_dados = presentes_dados

    @property
    def presentes_recebidos(self):
        return self.__presentes_recebidos

    @presentes_recebidos.setter
    def presentes_recebidos(self, presentes_recebidos):
        self.__presentes_recebidos = presentes_recebidos

    @property
    def partidas_jogadas(self):
        return self.__partidas_jogadas

    @partidas_jogadas.setter
    def partidas_jogadas(self, partidas_jogadas):
        self.__partidas_jogadas = partidas_jogadas

    @property
    def amigos(self):
        return self.__amigos

    @amigos.setter
    def amigos(self, amigos):
        self.__amigos = amigos

    @property
    def personagens(self):
        return self.__personagens

    @personagens.setter
    def personagens(self, personagens):
        self.__personagens = personagens

    @property
    def skins(self):
        return self.__skins

    @skins.setter
    def skins(self, skins):
        self.__skins = skins

    @property
    def chromas(self):
        return self.__chromas

    @chromas.setter
    def chromas(self, chromas):
        self.__chromas = chromas
    
    @property
    def historico_compras(self):
        return self.__historico_compras
    
    @historico_compras.setter
    def historico_compras(self, historico_compras):
        self.__historico_compras = historico_compras

