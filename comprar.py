from personagem import Personagem

class Comprar (AbstractcomprarController):
    
    def __init__(self, personagem: Personagem, jogador: Jogador)
        if isinstance(jogador, Jogador):
            self.__jogador = jogador
        if isinstance(personagem, Personagem):
            self.__personagem = personagem
        self.__amigos = []
        self.__inventario = []
        
