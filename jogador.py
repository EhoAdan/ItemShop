class Jogador
    
    def __init__(self, nome: str, saldo: int, dinheiro_gasto: int, amigo: Amigo)
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(saldo, int):
            self.__saldo = saldo
        if isinstance(dinheiro_gasto, int):
            self.__dinheiro_gasto = dinheiro_gasto
        self.__amigos = []
        self.__inventario = []
        
    @property
    def nome(self):
        return self.__nome

    @origem.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def saldo(self):
        return self.__saldo

    @origem.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    @property
    def dinheiro_gasto(self):
        return self.__dinheiro_gasto

    @origem.setter
    def dinheiro_gasto(self, dinheiro_gasto):
        self.__dinheiro_gasto = dinheiro_gasto
    
    @property
    def amigo(self):
        return self.__amigo

    @origem.setter
    def amigo(self, amigo):
        self.__amigo = amigo
    
    def adicionar_amigo(self, amigo: Amigo)
        if isinstance(amigo, Amigo):
            amigo = Amigo(nome, ID(?))
            if not (any(amigo.nome == nome
                    for amigo in self.__amigos)):
                self.__amigos.append(amigo)

    def excluir_amigo(self, amigo: Amigo)
        for amigo in self.__amigos:
            if amigo.nome == nome:
                self.__amigos.remove(amigo)
                break
    
    def adquirir_saldo(self, saldo: int)
    
    def presentear(self, inventario: itens.nome, amigo)
        #puxar inventario do amigo
    def comprar(self, saldo, inventario: itens.nome)
    