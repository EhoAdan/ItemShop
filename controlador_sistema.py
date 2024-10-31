from tela_sistema import TelaSistema
from controlador_loja import LojaController
from controlador_contas import ControladorContas
from controlador_jogador import ControladorJogador


class ControladorSistema:

    def __init__(self):
        self.__controlador_loja = ControladorSistema()
        self.__tela_sistema = TelaSistema()
        self.__controlador_conta = ControladorConta()
    
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
        login_on = {0: exit(),
                    1: self.__controlador_conta.registrar,
                    2: self.__controlador_conta.login}
        