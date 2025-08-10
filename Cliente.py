#------------- cadastro do cliente ------------
class Cliente:
    def __init__(self, nome, telefone, cpf):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf

    def exibir_info(self):
       print(f'Nome {self.nome}, Telefone {self.telefone}, Cpf {self.cpf}')

class SistemaCafeteria:
    def __init__(self):
       self.clientes = []

    def Cadastrar_Cliente(self): 
        nome = input('Nome do Cliente: ')
        telefone = input('Telefone(opcional): ')
        cpf = input('CPF: ')

        novo_cliente = Cliente(nome, telefone, cpf)
        self.clientes.append(novo_cliente)
        print('Cliente cadastrado com sucesso!')

    def lista_clientes(self):
        if not self.clientes:
            print('Nenhum cliente cadastrado!')
            return
        for cliente in self.clientes:
            cliente.exibir_info()

if __name__ == "__main__":
    sistema = SistemaCafeteria()

    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.Cadastrar_Cliente()
        elif opcao == "2":
            sistema.lista_clientes()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!") 

