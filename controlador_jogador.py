from jogador import Jogador
from tela_jogador import TelaJogador
from contas import Contas

class ControladorJogador:

    def __init__(self, jogador):
        self.__jogador = jogador
        self.__jogador_tela = TelaJogador()

    @property
    def jogador(self):
        return self.__jogador

    @property
    def jogador_tela(self):
        return self.__jogador_tela
    
    def fechar_jogo(self):
        print("Jogo encerrado")
        exit()

    def jogar_partida(self):
        self.__jogador.partidas_jogadas += 1
        print(f"Você jogou uma partida. Seu total de partidas é: {self.__jogador.partidas_jogadas}")
    
    def abrir_loja(self):
        #Se pá que vou deixar isso aqui pra você kkkkk
        #Só precisa fazer puxar as opções da loja, acho que até já tava pronto
        pass

    def gerenciar_amigos(self):
        acao_amigos = {0: exit, #Seria legal colocar uma mensagem 'jogo encerrado' aqui, mas o loop do While tá me complicando kk
                    1: self.adicionar_amigo,
                    2: self.excluir_amigo,
                    3: self.lista_amigos}
        while True:
            acao_amigos[self.__tela_jogador.jogador_opcoes_amigos()]()

    #Para excluir, é suficiente tirar da lista de jogadores? Acho que pra todos os efeitos, sim

    def excluir_conta(self):
        print("""Excluir sua conta é um processo permanente!
Tem certeza que deseja excluí-la?
0- Não, não desejo excluir minha conta.
9- Sim, desejo excluir minha conta.
""")   
        resposta = int(input())
        try:
            if resposta == 9:
                for jogador_excluido in self.__contas.jogadores:
                    if self.__jogador.nome == jogador_excluido.nome:
                        self.__contas.jogadores.remove(jogador_excluido)
                        print("Conta excluída com sucesso")
                        #Retornar para o menu inicial talvez?
                        exit()
            elif resposta == 0:
                print("Que bom que decidiu não excluir sua conta e continuar conosco!")
            return self.jogador_opcoes()
        except ValueError:
            print("Opção inválida! Retornando a tela inicial.")
            return self.jogador_opcoes()

    def eh_jogador(self, nome_jogador):
        for jogador_existe in self.__contas.jogadores:
            if jogador_existe.nome == nome_jogador.nome:
                return jogador_existe
        return None

    #DAQUI PRA BAIXO ESTAVA EM JOGADOR ANTES

    #Funciona
    def adicionar_amigo(self):
        nome_jogador = input("Digite o nome do jogador que quer adicionar: ")
        jogador_existe = self.eh_jogador(nome_jogador)
        if not isinstance(jogador_existe, Jogador):
            print("Houve uma tentativa de adicionar um não-jogador como amigo.")
        elif jogador_existe.nome == self.__jogador.nome:
            print("Você não pode se adicionar como amigo.")
        elif any(jogador_existe.nome == amigo.nome for amigo in self.__jogador.amigos):
            print(f"{jogador_existe.nome} já é seu amigo.")
        else:
            self.__jogador.__amigos.append(jogador_existe)
        return self.lista_amigos()

    #Funciona
    def excluir_amigo(self):
        amigo_excluir = input("Digite o nome do amigo que quer excluir: ")
        for amigo in self.__jogador.amigos:
            if amigo_excluir.nome == amigo.nome:
                self.__jogador.amigos.remove(amigo)
            return self.lista_amigos()

    #Funcionando
    def lista_amigos(self):
        print("Esta é sua lista atual de amigos:")
        for amigo in self.__amigos:
            print(amigo.nome)
        return self.gerenciar_amigos()
    
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

    def jogador_acoes(self):
        acoes_on = {0: exit, #Seria legal colocar uma mensagem 'jogo encerrado' aqui, mas o loop do While tá me complicando kk
                    1: self.__controlador_jogador.jogar,
                    2: self.__controlador_jogador.abrir_loja,
                    3: self.__controlador_jogador.gerenciar_amigos,
                    4: self.__controlador_jogador.excluir_conta}
        while True:
            acoes_on[self.__tela_jogador.jogador_opcoes()]()

    def alterar_compra_historico(self, entrada, mudanca):
        # Pega o índice da entrada a mudar, encontra a entrada e daí muda ela pra mudança
        self.__historico_compras[self.encontrar_compra_historico(entrada).index()] = mudanca
    
    def excluir_compra_historico(self, entrada):
        self.__historico_compras.pop(entrada)
