# --------------- Pedido ------------------
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.total = 0.0

    def adicionar_item(self, produto):
        self.itens.append(produto)

    def calcular_total(self):
        self.total = sum([produto.preco for produto in self.itens])
        return self.total

    def exibir_info(self):
        print(f"\n--- Pedido de {self.cliente.nome} ---")
        for produto in self.itens:
            print(f"{produto.nome} - R${produto.preco}")
        print(f"Total: R${self.total:.2f}")
        print("--------------------------")
