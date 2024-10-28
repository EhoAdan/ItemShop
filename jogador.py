import chroma
import personagem
import skin

class Jogador:
    
    def __init__(self, nome: str, saldo: int, dinheiro_gasto: int):
        if isinstance(nome, str):
            self.__nome = nome
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
    def personagens(self, personagens):
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
        self.__personagens.append(perso_novo)

    #Tentativa de fazer uma função só pra presente
    def presentear(self, item, amigo):
        if isinstance(item, personagem.Personagem):
            if personagem in self.__personagens and personagem not in amigo.__personagens:
                amigo.__personagens.append(personagem)
                self.__personagens.remove(personagem)
            else:
                if personagem not in self.__personagens:
                    print(f"Você não tem {personagem.nome}")
                elif personagem in amigo.__personagens:
                        print(f"Seu amigo já possui {personagem.nome}")
        elif isinstance(item, skin.Skin):
            if skin in self.__skin and skin not in amigo.__skin:
                amigo.__skin.append(skin)
                self.__skin.remove(skin)
            else:
                if skin not in self.__skin:
                    print(f"Você não tem {skin.nome}")
                elif skin in amigo.__skin:
                    print(f"Seu amigo já possui {skin.nome}")
        elif isinstance (item, chroma.Ch232roma):
            if chroma in self.__chroma and chroma not in amigo.__chroma:
                amigo.__chroma.append(chroma)
                self.__chroma.remove(chroma)
            else:
                if chroma not in self.__chroma:
                    print(f"Você não tem {chroma.nome}")
                elif chroma in amigo.__chroma:
                    print(f"Seu amigo já possui {chroma.nome}")
        else:
            print("O item selecionado não é presenteável")

    def comprar(self, saldo, inventario):
        pass
