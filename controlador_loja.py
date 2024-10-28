from personagem import Personagem
from skin import Skin
from chroma import Chroma
from jogador import Jogador
from loja import Loja
from tela_loja import TelaLoja

class LojaController:

    def __init__(self, loja = None, usuario = Jogador):
        # Acho que dá pra tirar o atributo jogador ou do controlador ou da loja
        if not loja or isinstance(loja, Loja):
            self.__loja = loja
        self.__tela_loja = TelaLoja()
        if isinstance(usuario, Jogador):
            self.__usuario = usuario

    def selecao_amigo(self):
        num_cada_pessoa = {1: self.__usuario}
        j = 1
        print("Para quem será a compra?")
        self.__tela_loja.tela_listar_pessoas(self.__usuario.amigos, j)
        for amigo in self.__usuario.amigos:
            j += 1
            num_cada_pessoa[j] = amigo
        pessoa_selecionada = self.__tela_loja.tela_seleciona_pessoa(j)
        if pessoa_selecionada == 0:
            return None
        return num_cada_pessoa[pessoa_selecionada]

    def selecao_personagem(self, lista_personagens, compra = False):
        num_cada_personagem = dict()
        print("""-------- Personagens ---------
Selecione um personagem:""")
        i = 1
        if compra:
            self.__tela_loja.tela_listar_itens_compra(lista_personagens, i)
        else:
            self.__tela_loja.tela_listar_itens(lista_personagens, i)
        for personagem in lista_personagens:
            # Insere valores crescentes para cada personagem
            num_cada_personagem[i] = personagem
            i += 1
        personagem_novo = self.__tela_loja.tela_selecao_personagem(i)
        if not personagem_novo:
            # Retorna para o menu anterior caso o usuário queira
            return None
        # Acessa o personagem baseado no dicionário e no número retornado
        return num_cada_personagem[personagem_novo]
    
    def selecao_skin(self, personagem, compra = False):
        num_cada_skin = dict()
        print("""-------- Skins ---------
Selecione uma skin:""")
        i = 1
        if compra:
            self.__tela_loja.tela_listar_itens_compra(personagem.skins, i)
        else:
            self.__tela_loja.tela_listar_itens(personagem.skins, i)
        for skin in personagem.skins:
            num_cada_skin[i] = skin
            i += 1
        skin_nova = self.__tela_loja.tela_selecao_skin(i)
        if not skin_nova:
            return None
        return num_cada_skin[skin_nova]
    
    def selecao_chroma(self, skin):
        num_cada_chroma = dict()
        print("""-------- Chromas ---------
Selecione um Chroma:""")
        i = 1
        self.__tela_loja.tela_listar_itens(skin.chromas, i)
        for chroma in skin.chromas:
            num_cada_chroma[i] = chroma
            i += 1
        chroma_novo = self.__tela_loja.tela_selecao_chroma(i)
        if not chroma_novo:
            return None
        return num_cada_chroma[chroma_novo]

    def compra_personagem_jogador(self):
        """Checa se é a classe necessária pra tudo e daí checa se o personagem existe,
        se o jogador já tem o personagem e se o saldo do jogador é suficiente, similar
        para outras de adicionar ao jogador.
        Ela cria um dicionário vazio e vai incluindo personagens por numero sequencialmente"""
        if len(self.__loja.personagens) != 0:
            while True:
                personagem_novo = self.selecao_personagem(self.__loja.personagens, True)
                if not personagem_novo:
                    return None
                if not personagem_novo.preco > self.__usuario.saldo:
                    break
                print(f"Compra inválida, você tem {self.__usuario.saldo} pontos e o personagem custa {personagem_novo.preco} pontos, tente novamente.")
        else:
            # Sai da função caso não haja nenhum personagem na loja por algum motivo
            print("Houve um erro no tamanho de personagens na loja.")
            return None
        recebedor_presente = self.selecao_amigo()
        if not recebedor_presente:
            # Sai caso a função retorne None
            return None
        if any(personagem_novo.__nome == personagem.__nome 
               for personagem in recebedor_presente.personagens):
            print("Usuário já possui este personagem.")
            return None

        """Provavelmente implementar compra de skins e chromas vai ser bem parecido
        mas com mais seleções no caminho da compra (pra qual personagem você quer a skin
        e pra qual skin você quer o chroma)"""

        self.__usuario.saldo -= personagem_novo.preco
        self.__usuario.add_p(personagem_novo)
        print(f"""Você acaba de comprar {personagem_novo.nome} para {recebedor_presente.nome}.
Você gastou {personagem_novo.preco} e possui {self.__usuario.saldo} pontos""")    
  
    def comprar_skin_jogador(self):
        if len(self.__loja.personagens) != 0 and len(self.__loja.skins):
            recebedor_presente = self.selecao_amigo()
            if not recebedor_presente:
            # Sai caso a função retorne None
                return None
            while True:
                personagem_p_skin = self.selecao_personagem(recebedor_presente.personagens)
                if len(personagem_p_skin.skins) != 0:
                    break
                #  Caso todo personagem vá ter pelo menos uma skin, na teoria isso não deve acontecer.
                print("O personagem selecionado não possui skins.")
            while True:
                skin_nova = self.selecao_skin(personagem_p_skin, True)
                if not skin_nova.preco > self.__usuario.saldo:
                    break
                print(f"Compra inválida, você tem {self.__usuario.saldo} pontos e a skin custa {skin_nova.preco} pontos, tente novamente.")
            if any(skin_nova.__nome == skin.nome 
                    for skin in recebedor_presente.skins):
                print("Usuário já possui esta skin.")
                return None
            self.__usuario.saldo -= skin_nova.preco
            self.__usuario.add_s(skin_nova)
            print(f"""Você acaba de comprar {skin_nova.nome} para {recebedor_presente.nome}.
Você gastou {skin_nova.preco} e possui {self.__usuario.saldo} pontos""")    

        else:
            print("Houve um erro na quantidade de personagens e/ou skins na loja.")
        """if isinstance(personagem, Personagem) and isinstance(skin_nova, Skin) and isinstance(jogador, Jogador):
            if not (any(skin_nova.nome == skin.nome
                        for skin in jogador.skins)) and jogador.saldo >= skin_nova.preco and skin_nova.nome not in personagem.__skins:
                jogador.saldo -= skin_nova.preco
                jogador.__skins.append(skin_nova)"""
   
    def comprar_chroma_jogador(self, skin_chroma: Skin, chroma_novo: Chroma, jogador: Jogador):
        if (isinstance(skin_chroma, Skin) and
           isinstance(chroma_novo, Chroma) and
           isinstance(jogador, Jogador)):
            if (not (any(chroma_novo.nome == chroma.nome
                        for chroma in jogador.chromas)) and
                    any(skin_chroma.nome == skin.nome for skin in jogador.skins) and
                    jogador.saldo >= chroma_novo.preco and
                    chroma_novo.nome in skin_chroma.__chromas):
                jogador.saldo -= chroma_novo.preco
                jogador.__chromas.append(chroma_novo)
    
    def adicionar_personagem_jogo(self, personagem_novo: Personagem):
        """Praticamente a mesma coisa de adicionar personagem ao jogador mas
        adiciona ao jogador (duh) e faz umas checagens diferentes, de novo, similar
        a adicionar as outras coisas ao jogo, talvez seja interessante passar atributos
        como argumentos e instanciar o personagem/skin/chroma dentro da função?
        Talvez também seja interessante passar essas funções para outro lugar"""
        if isinstance(personagem_novo, Personagem):
            if (not (any(personagem_novo.nome == personagem.nome 
                     for personagem in self.__loja.personagens))
                and personagem_novo.nome not in self.__loja.jogador.__personagens):
                self.__loja.personagens.append(personagem_novo)
    
    def adicionar_skin_jogo(self, skin_nova: Skin, personagem: Personagem):
        if (isinstance(skin_nova, Skin) and
            isinstance(personagem, Personagem) and
            any(personagem.nome == personagem_jogo.nome 
                for personagem_jogo in self.__loja.personagens) and not
            any(skin_nova.nome == skin_jogo.nome for skin_jogo in personagem.__skins)):
                personagem.skins.append(skin_nova)
                self.__loja.skins.append(skin_nova)
    
    def adicionar_chroma_jogo(self, skin: Skin, chroma_novo: Chroma):
        if (isinstance(skin, Skin) and
            isinstance(chroma_novo, Chroma) and
            any(skin.nome == personagem_jogo.nome 
                for personagem_jogo in self.__loja.personagens) and not
            any(chroma_novo.nome in chroma_jogo.nome for chroma_jogo in skin.__chromas)):
                self.__loja.chromas.append(chroma_novo)
                skin.chromas.append(chroma_novo)
    
    """Protótipo de uma função de retornar para a tela do sistema (Inclusive, vai precisar passar
    o controlador do sistema como um atributo)
    def retornar(self):
        self.__controlador_sistema.abre_tela()"""
    
    """Protótipo de invocador de tela
    def abre_tela(self):
        lista_opcoes = {1: self.compra_personagem_jogador(personagem, jogador),
                        2: self.compra_skin_jogador(personagem, skin, jogador),
                        3: self.compra_chroma_jogador(skin, personagem, jogador),
                        0: self.retornar}
        continua = True
        while continua:
            #Pelo que eu entendi, isso deixa a tela aberta até dar o retorno
            lista_opcoes[self.__tela_loja.tela_opcoes()]()"""
