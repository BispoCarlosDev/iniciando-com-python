class ContaBancaria:
    contasbancarias = []

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False
        ContaBancaria.contasbancarias.append(self)

    def __str__(self):
        return f'Titular: {self.titular} | Saldo: {self.saldo}'
    
    @classmethod
    def listar_contas(cls):
        for conta in ContaBancaria.contasbancarias:
            print(f'Titular: {conta.titular} | Saldo: {conta.saldo}')
    

conta01 = ContaBancaria('Carlos', 500)
conta02 = ContaBancaria('Pedro', 5000)

ContaBancaria.listar_contas()