class TelaLoja():
    def tela_opcoes(self):
        print("""-------- Loja ---------
Escolha sua opção:
1- Comprar um campeão
2- Comprar uma skin
3- Comprar um chroma
0- Sair do sistema
""")
        while True:
            try:
                opcao_usuario = int(input("Escolha uma opção: "))
                if not -1 < opcao_usuario < 4:
                    """Caso o usuário faça algo além de inserir 1, 2, 3 ou 0, já joga um valueerror logo,
                    já que é o que já tem a resposta de erro"""
                    raise ValueError
                return opcao_usuario
            except ValueError:
                print("Favor inserir uma opção válida.")
    
    def tela_selecionar_opcao_int(self, mensagem, limite_superior, limite_inferior):
        "Função que generaliza seleção de opções retornando int"
        while True:
            try:
                opcao_usuario = int(input(mensagem))
                if not limite_inferior <= opcao_usuario <= limite_superior:
                    raise ValueError
                return opcao_usuario
            except ValueError:
                print("Favor inserir um valor válido.")

    def tela_seleciona_pessoa(self, num_pessoas):
        return self.tela_selecionar_opcao_int("Selecione a pessoa pelo número: ", num_pessoas, 0)

    def tela_selecao_personagem(self, num_personagens):
        return self.tela_selecionar_opcao_int("Selecione o personagem pelo número: ", num_personagens, 1)