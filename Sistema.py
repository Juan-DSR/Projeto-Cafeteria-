# -------- Produto --------
class Produto: 
    def __init__(self, nome, preco, ingrediente, promo=False):
        self.nome = nome
        self.preco = preco
        self.ingrediente = ingrediente
        self.promo = promo
        
    def mostrar(self): # mostra as informações dos produtos é se esta em promoção 
        print(f"{self.nome} - R${self.preco:.2f}" + (" (promo!)" if self.promo else ""))
        print("Ingredientes:", self.ingrediente)
        print("-" * 25)


# -------- Cliente --------
class Cliente:
    def __init__(self, nome, telefone, cpf):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf

    def mostrar(self): # Mostra detalhes do cliente 
        print(f"{self.nome} | Tel: {self.telefone or '---'} | CPF: {self.cpf}")


# -------- Pedido --------
class Pedido: # representa o pedido do cliente 
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.total = 0.0

    def add_item(self, produto): # Adiciona um produto à lista de itens 
        self.itens.append(produto)

    def calc_total(self): 
        self.total = sum(p.preco for p in self.itens) # Calcula o preço total do pedido somando o preço dos itens escolhidos 
        return self.total

    def mostrar(self): # Mostra os detalhes do pedido junto ao preço total
        print(f"\n--- Pedido de {self.cliente.nome} ---")
        for p in self.itens:
            print(f"{p.nome} - R${p.preco:.2f}")
        print(f"Total: R${self.total:.2f}")
        print("-" * 25)


# -------- Sistema --------
class SistemaCafe: # gerencia todo o sistema da cafeteria 
    def __init__(self): # lista que armazena todos os clientes e produtos cadastrados  
        self.clientes = []
        self.produtos = [
            Produto("Café com Leite", 3.0, "Café, Leite"),
            Produto("Cappuccino", 7.0, "Café, Leite, Achocolatado", promo=True),
            Produto("Café Passado", 2.5, "Café, Água Fervente"),
            Produto("Brownie", 2.0, "Farinha, Chocolate, Açúcar"),
            Produto("Pão na Chapa", 4.0, "Pão, Manteiga", promo=True)
        ] 
        self.pedidos = []

    # ---- Clientes ----
    def novo_cliente(self): # pede os dados dos cliente para fazer  o cadastro e mandar para a lista de clientes cadastrados 
        nome = input('Nome: ')
        tel = input('Tel (opcional): ')
        cpf = input('CPF: ')
        self.clientes.append(Cliente(nome, tel, cpf))
        print('✔ Cliente Cadastrado')

    def ver_clientes(self): # Serve para ver a lista de clientes cadastrados
        if not self.clientes:
            print('Nenhum cliente cadastrado...')
            return
        for c in self.clientes:
            c.mostrar()

    # ---- Produtos ----
    def novo_produto(self): # pede os dados do produtos para fazer o cadastro dele no sistema
        nome = input('Nome do produto: ')
        ingr = input('Ingredientes: ')
        preco = float(input('Preço: '))
        promo = input('Promoção? (s/n): ').lower() == 's'
        self.produtos.append(Produto(nome, preco, ingr, promo))
        print('✔ Produto adicionado')

    def ver_produtos(self): # Mostra todos os produtos cadastrados e os detalhes dele 
        if len(self.produtos) == 0:
            print('Nenhum produto cadastrado...')
            return
        print('--- PRODUTOS ---')
        for p in self.produtos:
            p.mostrar()

    # ---- Pedidos ----
    def novo_pedido(self): # cria um pedido escolhendo um dos clientes cadastrado e os itens que o cliente escolher
        if not self.clientes:
            print("Cadastre um cliente primeiro!")
            return
        if not self.produtos:
            print("Cadastre um produto primeiro!")
            return

        print("\n--- CLIENTES ---")
        for i, c in enumerate(self.clientes):
            print(f"{i+1} - {c.nome}")
        try:
            idx_c = int(input("Cliente nº: ")) - 1
            cliente = self.clientes[idx_c]
        except (ValueError, IndexError):
            print("Número inválido!")
            return

        pedido = Pedido(cliente)

        while True:
            print("\n--- CARDÁPIO ---")
            for i, p in enumerate(self.produtos):
                print(f"{i+1} - {p.nome} - R${p.preco:.2f}")
            escolha = input("Produto nº (0 pra fechar): ")

            if escolha == "0":
                break

            try:
                pedido.add_item(self.produtos[int(escolha) - 1])
            except (ValueError, IndexError):
                print("Opção inválida, tente de novo.")

        if pedido.itens:
            pedido.calc_total()
            self.pedidos.append(pedido)
            print("\n✔ Pedido registrado")
            pedido.mostrar()
        else:
            print("Nenhum item adicionado.")

    def ver_pedidos(self): # mostra os pedidos ja feitos, com os detalhes e o preço total
        if not self.pedidos:
            print("Nenhum pedido registrado...")
            return
        for p in self.pedidos:
            p.mostrar()

# -------- Menu Principal --------
if __name__ == "__main__":
    sistema = SistemaCafe()

    while True:
        print("\n=== MENU ===")
        print("1 - Novo Cliente")
        print("2 - Ver Clientes")
        print("3 - Novo Produto")
        print("4 - Ver Produtos")
        print("5 - Novo Pedido")
        print("6 - Ver Pedidos")
        print("0 - Sair")
        op = input("> ")

        if op == "1":
            sistema.novo_cliente()
        elif op == "2":
            sistema.ver_clientes()
        elif op == "3":
            sistema.novo_produto()
        elif op == "4":
            sistema.ver_produtos()
        elif op == "5":
            sistema.novo_pedido()
        elif op == "6":
            sistema.ver_pedidos()
        elif op == "0":
            print("Saindoo...")
            break
        else:
            print("Opção inválida...")
