from conta import Conta

class Jogador:
    
    def __init__(self, nome: str, saldo: int, dinheiro_gasto: int):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(saldo, int):
            self.__saldo = saldo
        if isinstance(dinheiro_gasto, int):
            self.__dinheiro_gasto = dinheiro_gasto
        self.__amigos = []
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    @property
    def dinheiro_gasto(self):
        return self.__dinheiro_gasto

    @dinheiro_gasto.setter
    def dinheiro_gasto(self, dinheiro_gasto):
        self.__dinheiro_gasto = dinheiro_gasto
    
    @property
    def amigo(self):
        return self.__amigo

    @amigo.setter
    def amigo(self, amigo):
        self.__amigo = amigo
    
    def adicionar_amigo(self, amigo_novo):
        if isinstance(amigo_novo, Jogador):
            if not (any(amigo_novo.nome == amigo.nome
                    for amigo in self.__amigos)):
                self.__amigos.append(amigo_novo)

    def excluir_amigo(self, amigo_excluir):
        for amigo in self.__amigos:
            if amigo_excluir.nome == amigo.nome:
                self.__amigos.remove(amigo)
                break
    
    def adquirir_saldo(self):
        saldo = input("Insira o saldo a ser adquirido: ")
        if isinstance(saldo, int):
            saldo = int(saldo)
            self.saldo += saldo
            self.dinheiro_gasto += round(saldo * 0.02725, 2)
    
    def presentear(self, inventario, amigo):
        #puxar inventario do amigo
        pass

    def comprar(self, saldo, inventario):
        pass
