class Pessoa:

    def __init__(self, nome, id, email, senha):
        tudo_certo = True
        if not isinstance(nome, str):
            tudo_certo = False
            return None
        elif not isinstance(id, int):
            tudo_certo = False
            return None
        elif not isinstance(email, str):
            tudo_certo = False
            return None
        elif not isinstance(senha, str):
            tudo_certo = False
            return None
        if tudo_certo:
            self.nome = nome
            self.id = id
            self.email = email
            self.senha = senha
    
    
