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
        if isinstance(skins, Skin):
            self.__skins = skins
        if isinstance(chromas, Chroma):
            self.__chromas = chromas

    @property
    def jogador(self):
        return self.__jogador

    @property
    def personagens(self):
        return self.__personagens

    @property
    def skin(self):
        return self.__skin

    @property
    def chroma(self):
        return self.__chroma
