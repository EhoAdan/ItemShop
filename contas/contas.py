class Contas:

    def __init__(self, jogadores = [], admins = []):
        self.__jogadores = jogadores
        self.__admins = admins

    @property
    def jogadores(self):
        return self.__jogadores
   
    @jogadores.setter
    def jogadores(self, jogadores):
        self.__jogadores = jogadores

    @property
    def admins(self):
        return self.__admins

    @admins.setter
    def admins(self, admins):
        self.__admins = admins
