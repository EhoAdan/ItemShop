class TelaLoja():
    def tela_opcoes(self):
        print("""-------- Loja ---------
Escolha sua opção:
1- Campeões
2- Skins
3- Cromas
0- Finalizar sistema
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

