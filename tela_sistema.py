class TelaSistema():
    
    def menu_opcoes(self):
        print("""-------- Entrada ---------
0- Fechar o programa
1- Registrar uma conta nova
2- Fazer login em uma conta
""")
        return self.tela_selecionar_opcao_int("Selecione uma opção: ", 2, 0)
    
    def tela_selecionar_opcao_int(self, mensagem, limite_superior, limite_inferior):
        while True:
            try:
                opcao_usuario = int(input(mensagem))
                if not limite_inferior <= opcao_usuario <= limite_superior:
                    raise ValueError
                return opcao_usuario
            except ValueError:
                print("Favor inserir um valor válido.")