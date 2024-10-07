import Personagem
import Skin
import Chroma
import Jogo
import Jogador


class Loja:
    
    def __init__(self, personagem: Personagem, jogador: Jogador, jogo: Jogo, skin: Skins, chroma: Chroma)
        if isinstance(personagem, Personagem):
            self.__personagem = personagem
        if isinstance(jogador, Jogador):
            self.__jogador = jogador
        if isinstance(jogo, Jogo):
            self.__jogo = jogo
        if isinstance(skin, Skin):
            self.__skin = skin
        if isinstance(chroma, Chroma):
            self.__chroma = chroma

    @property
    def jogador(self):
        return self.__jogador

    @property
    def personagem(self):
        return self.__personagem

    @property
    def jogo(self):
        return self.__jogo

    @property
    def skin(self):
        return self.__skin

    @property
    def chroma(self):
        return self.__chroma
