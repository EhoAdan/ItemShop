from personagem import Personagem
from skin import Skin
from chroma import Chroma
from jogo import Jogo
from jogador import Jogador
from loja import Loja

class LojaController:

    def __init__(self, jogador: Jogador, personagens = [], skins = [], chromas = []):
                    self.__personagens = personagens
                    self.__jogador = jogador
                    self.__skins = skins
                    self.__chromas = chromas

    def adicionar_personagem(self, personagem_novo: Personagem, jogador: Jogador):
        if isinstance(personagem_novo, Personagem) and isinstance(jogador, Jogador):
            if (not (any(personagem_novo.nome == personagem.nome 
                        for personagem in jogador.__personagens)) and jogador.saldo >= personagem_novo.preço 
                        and personagem_novo.nome not in jogador.__personagens):
                jogador.saldo -= personagem_novo.preço
                jogador.__personagens.append(personagem_novo)
    
    def adicionar_skin(self, personagem: Personagem, skin_nova: Skin, jogador: Jogador):
        if isinstance(personagem, Personagem) and isinstance(skin_nova, Skin) and isinstance(jogador, Jogador):
            if not (any(skin_nova.nome == skin.nome
                        for skin in jogador.skins)) and jogador.saldo >= skin_nova.preço and skin_nova.nome not in personagem.__skins:
                jogador.saldo -= skin_nova.preço
                jogador.__skins.append(skin_nova)
    
    def adicionar_chroma(self, personagem: Personagem, skin: Skin, chroma_novo: Chroma, jogador: Jogador):
        if (isinstance(personagem, Personagem) and
           isinstance(skin, Skin) and
           isinstance(chroma_novo, Chroma) and
           isinstance(jogador, Jogador)):
            if (not (any(chroma_novo.nome == chroma.nome
                        for chroma in jogador.chromas)) and
                    jogador.saldo >= chroma_novo.preço and
                    chroma_novo.nome in skin.__chromas):
                jogador.saldo -= chroma_novo.preço
                jogador.__chromas.append(chroma_novo)
