class TelaLoja():
    def loja_opcoes(self):
        print("""-------- Loja ---------
Escolha sua opção:
1- Comprar um campeão
2- Comprar uma skin
3- Comprar um chroma
0- Sair do sistema
""")
        self.tela_selecionar_opcao_int("Selecione uma opção:", 3, 0)

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
    
    def tela_listar_itens(self, lista_itens, numero_inicial):
        print("0: Retornar")
        for item in lista_itens:
            print(f"{numero_inicial}: {item.nome}.")
            numero_inicial += 1

    def tela_listar_itens_compra(self, lista_itens, numero_inicial):
        print("0: Retornar")
        for item in lista_itens:
            print(f"{numero_inicial}: {item.nome} por {item.preco} pontos.")
            numero_inicial += 1

    def tela_listar_pessoas(self, lista_pessoas, numero_inicial):
        print(f"""0: Retornar.
{numero_inicial}: Você mesmo.""")
        for pessoa in lista_pessoas:
            numero_inicial += 1
            print(f"{numero_inicial}: {pessoa.nome}.")

    def tela_seleciona_pessoa(self, num_pessoas):
        return self.tela_selecionar_opcao_int("Selecione a pessoa pelo número: ", num_pessoas, 0)

    def tela_selecao_personagem(self, num_personagens, compra = False):
        return self.tela_selecionar_opcao_int("Selecione o personagem pelo número: ", num_personagens, 0)

    def tela_selecao_skin(self, num_skins, compra = False):
        return self.tela_selecionar_opcao_int("Selecione a skin pelo número: ", num_skins, 0)
    
    def tela_selecao_chroma(self, num_chromas):
        return self.tela_selecionar_opcao_int("Selecione o chroma pelo número", num_chromas, 0)
