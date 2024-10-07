class Jogo

    def __init__(self, jogador: str, admin: str)
        if isinstance(jogador, str):
            self.__jogador = jogador
        if isinstance(admin, str):
            self.__admin = admin
        self.__jogadores = []
        self.__admins = []
        
    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador

    @property
    def admin(self):
        return self.__admin

    @admin.setter
    def admin(self, admin):
        self.__admin = admin
    
    def incluir_jogador(self, jogador: Jogador):
        if isinstance(jogador, Jogador):
            if jogador not in self.__jogadores:
                self.__jogadores.append(jogador)
    
    def banir_jogador(self, jogador: Jogador)
        #O jogador ainda existe, mas não consegue mais interagir com o jogo
        #(não é possível inserir outro com nome igual)
