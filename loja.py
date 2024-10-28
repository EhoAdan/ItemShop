from personagem import Personagem
from skin import Skin
from chroma import Chroma
from jogador import Jogador
from admin import Admin


class Loja:
 
    def __init__(self, jogador: Jogador, personagens = [], skins = [], chromas = []):
        if isinstance(personagens, list):
            self.__personagens = personagens
        if isinstance(jogador, Jogador):
            self.__jogador = jogador
        if isinstance(skins, list):
            self.__skins = skins
        if isinstance(chromas, list):
            self.__chromas = chromas

    @property
    def jogador(self):
        return self.__jogador

    @property
    def personagens(self):
        return self.__personagens

    @property
    def skins(self):
        return self.__skins

    @property
    def chromas(self):
        return self.__chromas
