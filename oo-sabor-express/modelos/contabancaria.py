class ContaBancaria:
    contasbancarias = []

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contasbancarias.append(self)

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    #def __str__(self):
    #    return f'Titular: {self._titular} | Saldo: {self._saldo}'
    
    @classmethod
    def listar_contas(cls):
        for conta in ContaBancaria.contasbancarias:
            print(f'Titular: {conta._titular} | Saldo: {conta._saldo} | {conta._ativo}')

    def ativar_conta(self):
        self._ativo = not self._ativo
    

conta01 = ContaBancaria('Carlos', 500)
conta02 = ContaBancaria('Pedro', 5000)

ContaBancaria.listar_contas()

conta01.ativar_conta()

ContaBancaria.listar_contas()