from tela_sistema import TelaSistema
from controlador_loja import LojaController


class ControladorSistema:

    def __init__(self):
        self.__controlador_loja = ControladorSistema
        self.__tela_sistema = TelaSistema
    
    @property
    def controlador_loja(self):
        return self.__controlador_loja
    
    @property
    def tela_sistema(self):
        return self.__tela_sistema
    
    