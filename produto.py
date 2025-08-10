#------------- criando os produtos --------------------
class Produto:
    def __init__(self, nome, preco, ingrediente, em_promocao=False):
        self.nome = nome
        self.preco = preco
        self.ingrediente = ingrediente
        self.em_promocao = em_promocao
        
    def exibir_info(self):
        if self.em_promocao:
            print(f"{self.nome} - R${self.preco} (em promoção!)")
        else:
            print(f"{self.nome} - R${self.preco}")
        print(f"Ingredientes: {self.ingrediente}")
        print("------------------------")

class SistemaCafeteria:
    def __init__(self):
        self.produtos = [
            Produto("Café com Leite", 3.0, "Café, Leite"),
            Produto("Cappuccino", 7, "Café, Leite, Achocolatado", em_promocao=True),
            Produto("Café Passado", 2.5, "Café, Água Fervente"),
            Produto("Brownies", 2, "Farinha de Trigo, Chocolate meio Amargo, Açúcar"),
            Produto("Pão na Chapa", 4, "Pão Françes, Manteiga", em_promocao=True)
        ]

    def cadastrar_produto(self):
        nome = input('Nome do produto: ')
        ingredientes = input('Ingredientes: ')
        preco = float(input('Preço do Produto: '))
        promo = input('Está em promoção? (s/n): ')
        em_promocao = True if promo.lower() == 's' else False

        novo_produto = Produto(nome, preco, ingredientes, em_promocao)
        self.produtos.append(novo_produto)
        print('Produto cadastrado com sucesso!\n')

    def listar_produtos(self):
        if not self.produtos:
            print('Nenhum produto cadastrado.\n')
        else:
            print('--- PRODUTOS ---')
            for produto in self.produtos:
                produto.exibir_info()
    
if __name__ == "__main__":
    sistema = SistemaCafeteria()

    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.cadastrar_produto()
        elif opcao == "2":
            sistema.listar_produtos()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!") 
    
