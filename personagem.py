from skin import Skin

class Personagem:

    def __init__(self, nome: str, preco: int):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(preco, int):
            self.__preco = preco
        self.__skins = []
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco
    
    @property
    def skins(self):
        return self.__skins
    
    @skins.setter
    def skins(self, skins):
        self.__skins = skins
    
    def incluir_skin(self, nome: str, preco: int):
        if isinstance(nome, str) and isinstance(preco, int):
            skin = Skin(nome, int)
            if not (any(skin.nome == nome
                    for skin in self.__skins)):
                self.__skins.append(skin)

    def excluir_skin(self, nome: str):
        for skin in self.__skins:
            if skin.nome == nome:
                self.__skins.remove(skin)
                break

