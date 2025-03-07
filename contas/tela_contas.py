class TelaConta():

    def conta_opcoes(self):
        print("""-------- TelaInicial ---------
Escolha sua opção:
1- Criar nova conta
2- Log in
0- Sair do sistema
""")

        while True:
            try:
                opcao_usuario = int(input("Escolha uma opção: "))
                if not -1 < opcao_usuario < 3:
                    """Caso o usuário faça algo além de inserir 1, 2, 3 ou 0, já joga um valueerror logo,
                    já que é o que já tem a resposta de erro"""
                    raise ValueError
                return opcao_usuario
            except ValueError:
                print("Favor inserir uma opção válida.")
