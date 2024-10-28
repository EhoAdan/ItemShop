from chroma import Chroma

class Skin:

    def __init__(self, nome: str, preco: int):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(preco, int):
            self.__preco = preco
        self.__chromas = []
    
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
    def chromas(self):
        return self.__chromas
    
    @chromas.setter
    def chromas(self, chromas):
        self.__chromas = chromas
    
    def incluir_chroma(self, nome: str):
        if isinstance(nome, str):
            chroma = Chroma(nome)
            if not (any(chroma.nome == nome
                    for chroma in self.__chromas)):
                self.__chromas.append(chroma)

    def excluir_chroma(self, nome: str):
        for chroma in self.__chromas:
            if chroma.nome == nome:
                self.__chromas.remove(chroma)
                break
