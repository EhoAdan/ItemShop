from conta import Conta

class Personagem:
    
    def __init__(self, nome: str, preco: int):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(preco, int):
            self.__preco = preco
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def nome(self):
        return self.__nome

class Jogador:
    
    def __init__(self, nome: str, id: str, saldo: int, dinheiro_gasto: int):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(id, str):
            self.__id = id
        if isinstance(saldo, int):
            self.__saldo = saldo
        if isinstance(dinheiro_gasto, int):
            self.__dinheiro_gasto = dinheiro_gasto
        self.__amigos = []
        self.__personagens = []
        self.__skins = []
        self.__chromas = []
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

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
    def amigos(self):
        return self.__amigos

    @amigos.setter
    def amigos(self, amigos):
        self.__amigos = amigos
    
    @property
    def personagens(self):
        return self.__personagens

    @personagens.setter
    def personagens(self, amigos):
        self.__personagens = personagens

    @property
    def skins(self):
        return self.__skins

    @skins.setter
    def skins(self, skins):
        self.__skins = skins

    @property
    def chromas(self):
        return self.__chromas

    @chromas.setter
    def chromas(self, chromas):
        self.__chromas = chromas

    #Funciona
    def adicionar_amigo(self, amigo_novo):
        if isinstance(amigo_novo, Jogador):
            if not (any(amigo_novo.nome == amigo.nome
                    for amigo in self.__amigos)):
                self.__amigos.append(amigo_novo)
            else:
                print(f"{amigo_novo.nome} já é seu amigo")

    #Funciona
    def excluir_amigo(self, amigo_excluir):
        for amigo in self.__amigos:
            if amigo_excluir.nome == amigo.nome:
                self.__amigos.remove(amigo)
                break

    #Funcionando
    def lista_amigos(self):
        for amigo in self.__amigos:
            print(amigo.nome)
    
    #Funcionando
    def lista_personagens(self):
        for perso in self.__personagens:
            print(perso.nome)

    #Funcionando
    def lista_skin(self):
        for skin in self.__skins:
            print(skin.nome)

    #Funcionando
    def lista_chroma(self):
        for chroma in self.__chromas:
            print(chroma.nome)

    #Funciona
    def adquirir_saldo(self):
        while True:
            try:
                saldo = int(input("Insira o saldo a ser adquirido: "))
                break
            except ValueError:
                print("Por favor, insira um número inteiro")
                pass

        saldo = int(saldo)
        self.__saldo += saldo
        self.__dinheiro_gasto += round(saldo * 0.02725, 2)

    def add_p(self, perso_novo):
        if not (any(perso_novo.nome == personagem.nome
                for perso in self.__personagens)):
            self.__personagens.append(perso_novo)
        else:
            print(f"{perso_novo.nome} já está em seu inventário")
    
    #talvez tenhamos que fazer uma função para cada item
    #mas a Prof disse que pode ser possível fazer uma só
    #caso consigamos checar que tipo de objeto temos dentro
    #da função
    def presentear_personagem(self, personagem, amigo):
        if personagem.nome in self.__personagens and personagem.nome not in amigo.__personagens:
            amigo.__personagens.append(personagem)
            self.__personagens.remove(personagem)
        else:
            print(f"Você não tem {personagem.nome} ou seu amigo já possui {personagem.nome}")
        pass

    def comprar(self, saldo, inventario):
        pass

Jogador1 = Jogador("Akmenos", "010101", 0, 0)
Jogador2 = Jogador("Gabigol", "020202", 0, 0)
Jogador3 = Jogador("SupaMario", "030303", 0, 0)
P1 = Personagem("Anaís", 3000)
P2 = Personagem("Darwin", 450)
P3 = Personagem("Gumble", 1200)

Jogador1.lista_personagens()
Jogador1.add_p(P1)
Jogador1.lista_personagens()
Jogador1.presentear_personagem(P1, Jogador2)
Jogador1.lista_personagens()
Jogador2.lista_personagens()
