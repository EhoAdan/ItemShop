from personagem import Personagem


class Jogador:
    
    def __init__(self, nome: str, email: str, senha: str, saldo: int = 0, dinheiro_gasto: int = 0):
        # acho que a gente faz essa checagem de tipos na hora de criar a conta
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__saldo = saldo
        self.__dinheiro_gasto = dinheiro_gasto
        self.__amigos = []
        self.__personagens = []
        self.__skins = []
        self.__chromas = []
        self.__historico_compras = []

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
    
    @property
    def historico_compras(self):
        return self.__historico_compras
    
    @historico_compras.setter
    def historico_compras(self, historico_compras):
        self.__historico_compras = historico_compras

    #Funciona
    # Gabriel: Adicionei uma checagem pra não se adicionar como amigo e diminuí a quantidade
    # de aninhamento nas checagens
    # Provavelmente isso tudo abaixo vai ter que mandar pro controlador
    def adicionar_amigo(self, amigo_novo):
        if not isinstance(amigo_novo, Jogador):
            print("Houve uma tentativa de adicionar um não-jogador como amigo.")
        elif amigo_novo.nome == self.__nome:
            print("Você não pode se adicionar como amigo.")
        elif any(amigo_novo.nome == amigo.nome for amigo in self.__amigos):
            print(f"{amigo_novo.nome} já é seu amigo.")
        else:
            self.__amigos.append(amigo_novo)

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
    
    def add_s(self, skin_nova):
        self.__skins.append(skin_nova)
    
    def add_c(self, chroma_novo):
        self.__chromas.append(chroma_novo)
    
    def adicionar_compra_historico(self, compra_dados):
        self.__historico_compras.append(compra_dados)
    
    def exibir_historico(self):
        for compra in self.__historico_compras:
            print(compra)
    
    def encontrar_compra_historico(self, dado):
        # exemplo: encontrar_compra_historico("ornn")
        resultado = None
        pass

    def alterar_compra_historico(self, entrada, mudanca):
        # Pega o índice da entrada a mudar, encontra a entrada e daí muda ela pra mudança
        self.__historico_compras(self.encontrar_compra_historico(entrada).index()) = mudanca
    
    def excluir_compra_historico(self, entrada):
        self.__historico_compras.pop(entrada)

        
