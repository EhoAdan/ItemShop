class Amigo:

    def __init__(self, nome: str)
        if isinstance(nome, str):
            self.__nome = nome
        self.__inventario = []
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
