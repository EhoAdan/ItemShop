class Admin:
    def __init__(self, nome, id, email, senha):
        if (isinstance(nome, str) and isinstance(id, int) and 
            isinstance(email, str) and isinstance(senha, str)):
            self.__nome = nome
            self.__id = id
            self.__email = email
            self.__senha = senha

    def __init__(self, nome, id, email, senha):
        if (isinstance(nome, str) and isinstance(id, int) and 
            isinstance(email, str) and isinstance(senha, str)):
            self.__nome = nome
            self.__id = id
            self.__email = email
            self.__senha = senha
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
    
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