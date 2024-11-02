class TelaJogador():

    def jogador_opcoes(self):
        print("""-------- O que você quer fazer? ---------
0- Fechar o Jogo
1- Jogar partida
2- Loja
3- Amigos
4- Excluir conta
""")
        return self.jogador_selecionar_opcao_int("Selecione uma opção: ", 4, 0)
    
    def jogador_selecionar_opcao_int(self, mensagem, limite_superior, limite_inferior):
        while True:
            try:
                opcao_usuario = int(input(mensagem))
                if not limite_inferior <= opcao_usuario <= limite_superior:
                    raise ValueError
                return opcao_usuario
            except ValueError:
                print("Favor inserir uma opção válida.")
