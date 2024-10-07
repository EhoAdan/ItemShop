class Chroma

    def __init__(self, nome: str, preco: int)
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(preco, int):
            self.__preco = preco
    
    @property
    def nome(self):
        return self.__nome

    @origem.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco

    @origem.setter
    def preco(self, preco):
        self.__preco = preco  