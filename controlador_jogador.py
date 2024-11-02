from jogador import Jogador
from tela_jogador import TelaJogador

class ControladorJogador:

    def __init__(self, jogador):
        self.__jogador = jogador
        self.__jogador_tela = TelaJogador()

    @property
    def jogador(self):
        return self.__jogador

    @property
    def jogador_tela(self):
        return self.__jogador_tela
    
    def jogar(self):
        self.__jogador.partidas_jogadas += 1
    
    def abrir_loja(self):
        pass
