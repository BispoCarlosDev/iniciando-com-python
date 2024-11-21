class ClienteBanco:
    clientesbanco = []

    def __init__(self, nome, numero_conta, cpf, idade, estado_civil):
        self._nome = nome
        self._numero_conta = numero_conta
        self._cpf = cpf
        self._idade = idade
        self._estado_civil = estado_civil
        ClienteBanco.clientesbanco.append(self)

    def __str__(self):
        return f'{self._nome} | {self._numero_conta} | {self._cpf} | {self._idade} | {self._estado_civil}'

    @classmethod
    def listar_clientes(cls):
        print(f'{'Nome Cliente'.ljust(20)} | {'Número da Conta'.ljust(20)} | {'Cpf'.ljust(20)} | {'Idade Cliente'.ljust(20)} | {'Estado Civil'}')
        for cliente in cls.clientesbanco:
            print(f'{cliente._nome.ljust(20)} | {cliente._numero_conta.ljust(20)} | {cliente._cpf.ljust(20)} | {cliente._idade.ljust(20)} | {cliente._estado_civil}')

ClienteBanco('Carlos', '12345', '12312312312', '23', 'Solteiro')
ClienteBanco('Pedro', '54321', '45645645645', '32', 'Casado')
ClienteBanco('João', '67890', '78978978978', '20', 'Solteiro')

ClienteBanco.listar_clientes()