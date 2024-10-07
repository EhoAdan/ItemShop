import Personagem


class Inventario:
    
    def __init__(self, personagem: Personagem, jogador: Jogador)
        if isinstance(jogador, Jogador):
            self.__jogador = jogador
        if isinstance(personagem, Personagem):
            self.__personagem = personagem

    @property
    def jogador(self):
        return self.__jogador

    @property
    def personagem(self):
        return self.__personagem
