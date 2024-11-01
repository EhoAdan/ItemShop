from tela_sistema import TelaSistema
from controlador_loja import ControladorLoja, Loja, Jogador, Skin, Personagem
from controlador_contas import ControladorContas, Contas
from controlador_jogador import ControladorJogador


class ControladorSistema:

    def __init__(self, loja, contas):
        self.__controlador_loja = ControladorLoja(loja)
        self.__tela_sistema = TelaSistema()
        self.__controlador_contas = ControladorContas(contas)
        self.__usuario = None
        self.login_ou_registrar()
    
    @property
    def controlador_loja(self):
        return self.__controlador_loja
    
    @property
    def tela_sistema(self):
        return self.__tela_sistema
    
    @property
    def controlador_conta(self):
        return self.__controlador_conta
    
    def login_ou_registrar(self):
        login_on = {0: exit,
                    1: self.__controlador_contas.registrar,
                    2: self.__controlador_contas.login}
        while True:
            login_on[self.__tela_sistema.menu_opcoes()]()

amale = Jogador("Amale", "amale@gmail.com", "amale123", 9999999)
tchali = Jogador("Tchali", "tchali123@gmail.com.br", "tchali123")
ornn = Personagem("Ornn", 4800)
ornn_trovao = Skin("Ornn Deus do Trovão", 900)
loja = Loja(amale, [ornn], [ornn_trovao])
contas = Contas([amale, tchali])
sistema = ControladorSistema(loja, contas)