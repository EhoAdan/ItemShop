class Conta:

    def __init__(self, nome, email, senha):
        if (isinstance(nome, str) and 
            isinstance(email, str) and isinstance(senha, str)):
            self.__nome = nome
            self.__email = email
            self.__senha = senha
    
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
