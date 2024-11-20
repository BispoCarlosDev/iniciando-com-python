class Cliente:

    clientes = []

    def __init__(self, nome, cpf, telefone, idade):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.idade = idade
        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.cpf} | {self.telefone} | {self.idade}'
    
    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'{cliente.nome} | {cliente.cpf} | {cliente.telefone} | {cliente.idade}')

cliente_carlos = Cliente('Carlos', '70707070707', '40028922', 23)
cliente_pedro = Cliente('Pedro', '70707070707', '40028922', 32)
cliente_joao = Cliente('João', '70707070707', '40028922', 20)

Cliente.listar_clientes()