from personagem import Personagem
from skin import Skin
from chroma import Chroma
from jogador import Jogador
from loja import Loja
from tela_loja import TelaLoja

class LojaController:

    def __init__(self, loja = None, usuario = Jogador):
        if not loja or isinstance(loja, Loja):
            self.__loja = loja
        self.__tela_loja = TelaLoja()
        if isinstance(usuario, Jogador):
            self.__usuario = usuario

    def adicionar_personagem_jogador(self, personagem_novo: Personagem, jogador: Jogador):
        """Checa se é a classe necessária pra tudo e daí checa se o personagem existe,
        se o jogador já tem o personagem e se o saldo do jogador é suficiente, similar
        para outras de adicionar ao jogador.
        Acho que tem que invocar uma tela pra selecionar o personagem e o jogador dentro
        da função e tirar dos argumentos da própria função.
        Ela cria um dicionário vazio e vai incluindo personagens por numero sequencialmente"""
        if len(self.__loja.personagens) != 0:
            num_cada_personagem = dict()
            print("""-------- Personagens ---------
Selecione um personagem:""")
            i = 1
            for personagem in self.__loja.personagens:
                num_cada_personagem[i] = personagem
                print(f"{i}: {personagem.nome} por {personagem.__preco} pontos.")
                i += 1
            print(f"{i + 1}: Retornar")
            while True:
                personagem_novo = self.__tela_loja.tela_compra_personagem(i)
                if personagem_novo == i + 1:
                    # Retorna para o menu anterior caso o usuário queira
                    return None
                # Acessa o personagem baseado no dicionário e no número retornado
                personagem_novo = num_cada_personagem[self.__tela_loja.tela_compra_personagem(i)]
                if not personagem_novo.__preco > self.__usuario.__saldo:
                    break
                print(f"Compra inválida, você tem {self.__usuario.__saldo} pontos e o personagem custa {personagem_novo.__preco} pontos, tente novamente.")
        num_cada_pessoa = {self.__usuario: 0}
        j = 1
        print("0: Presentear à si mesmo")
        for amigo in self.__usuario.__amigos:
            num_cada_pessoa[j] = amigo
            print(f"{j}: {amigo.__nome}")
            j += 1
        print(f"{j + 1}: Retornar")
        recebedor_presente = self.__tela_loja.tela_seleciona_pessoa(j)
        if recebedor_presente == j + 1:
            return None
        recebedor_presente = num_cada_pessoa[recebedor_presente]
        if any(personagem_novo.__nome == personagem.__nome 
               for personagem in recebedor_presente.__personagens):
            print("Usuário já possui este personagem.")
            return None
        recebedor_presente.add_p(personagem_novo)

        """Provavelmente implementar compra de skins e chromas vai ser bem parecido
        mas com mais seleções no caminho da compra (pra qual personagem você quer a skin
        e pra qual skin você quer o chroma)"""


        if (not (any(personagem_novo.nome == personagem.nome 
                 for personagem in jogador.__personagens)) and jogador.saldo >= personagem_novo.preco 
                 and personagem_novo.nome not in jogador.__personagens):
            jogador.saldo -= personagem_novo.preco
            jogador.__personagens.append(personagem_novo)
  
    def adicionar_skin_jogador(self, personagem: Personagem, skin_nova: Skin, jogador: Jogador):
        if isinstance(personagem, Personagem) and isinstance(skin_nova, Skin) and isinstance(jogador, Jogador):
            if not (any(skin_nova.nome == skin.nome
                        for skin in jogador.skins)) and jogador.saldo >= skin_nova.preco and skin_nova.nome not in personagem.__skins:
                jogador.saldo -= skin_nova.preco
                jogador.__skins.append(skin_nova)
   
    def adicionar_chroma_jogador(self, skin_chroma: Skin, chroma_novo: Chroma, jogador: Jogador):
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
        lista_opcoes = {1: self.adicionar_personagem_jogador(personagem, jogador),
                        2: self.adicionar_skin_jogador(personagem, skin, jogador),
                        3: self.adicionar_chroma_jogador(skin, personagem, jogador),
                        0: self.retornar}
        continua = True
        while continua:
            #Pelo que eu entendi, isso deixa a tela aberta até dar o retorno
            lista_opcoes[self.__tela_loja.tela_opcoes()]()"""
