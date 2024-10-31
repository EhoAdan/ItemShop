class Contas:

    def __init__(self):
        self.__jogadores = []
        self.__admins = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

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
