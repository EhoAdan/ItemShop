import Jogador
import Personagem
import Skin
import Chroma
import Inventario

class LojaController:

    def __init__(self, personagem: Personagem, jogador: Jogador,
                       skin: Skin, chroma: Chroma,
                       inventario: Inventario):
                        self.__personagem = personagem
                        self.__jogador = jogador
                        self.__skin = skin
                        self.__chroma = chroma
                        self.__inventario = inventario

    def adicionar_personagem(self, personagem: Personagem, jogador: Jogador)
        if isinstance(personagem, Personagem) and
           isinstance(jogador, Jogador):
            personagem = Personagem(preço, nome)
            if not (any(personagem.nome == nome
                        for personagem in jogador.__personagens)) and
                    jogador.saldo >= personagem.preço and
                    personagem.nome in inventario.__personagens:
            jogador.saldo = jogador.saldo - personagem.preço
            jogador.__personagens.append(personagem)
    
    def adicionar_skin(self, personagem: Personagem, skin: Skin, jogador: Jogador)
        if isinstance(personagem, Personagem) and
           isinstance(skin, Skin) and
           isinstance(jogador, Jogador):
            skin = Skin(preço, nome)
            if not (any(skin.nome == nome
                        for skin in jogador.__skins)) and
                    jogador.saldo >= skin.preço and
                    skin.nome in personagem.__skins:
            jogador.saldo = jogador.saldo - skin.preço
            jogador.__skins.append(skin)
    
    def adicionar_chroma(self, personagem: Personagem, skin: Skin,
                         chroma: Chroma jogador: Jogador)
        if isinstance(personagem, Personagem) and
           isinstance(skin, Skin) and
           isinstance(chroma, Chroma) and
           isinstance(jogador, Jogador):
            chroma = Chroma(preço, nome)
            if not (any(chroma.nome == nome
                        for chroma in jogador.__chromas)) and
                    jogador.saldo >= chroma.preço and
                    chroma.nome in skin.__chromas:
            jogador.saldo = jogador.saldo - chroma.preço
            jogador.__chromas.append(chroma)
