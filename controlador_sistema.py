from tela_sistema import TelaSistema
from loja.controlador_loja import ControladorLoja, Loja, Jogador, Skin, Personagem
from contas.controlador_contas import ControladorContas, Contas
from jogador.controlador_jogador import ControladorJogador


amale = Jogador("Amale", "amale@gmail.com", "amale123", 9999999)
tchali = Jogador("Tchali", "tchali123@gmail.com.br", "tchali123")
ornn = Personagem("Ornn", 4800)
ornn_trovao = Skin("Ornn Deus do Trovão", 900)
loja = Loja(amale, [ornn], [ornn_trovao])
contas = Contas([amale, tchali])

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

    def login_ou_registrar(self):
        login_on = {0: exit,
                    1: self.__controlador_contas.registrar,
                    2: self.__controlador_contas.login}
        while True:
            login_on[self.__tela_sistema.menu_opcoes()]()

sistema = ControladorSistema(loja, contas)