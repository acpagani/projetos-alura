class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'TITULAR: {self._titular} | SALDO: {self._saldo} | ESTADO: {self.ativo}'

    def ativar_conta(self):
        self._ativo = True

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo


conta1 = ContaBancaria('Roberto', 2500)
conta1.ativar_conta()
print(conta1.titular)


class ClienteBanco:
    def __init__(self, nome='', idade='', profissao='', saldo=0):
        self._nome = nome
        self._idade = idade
        self.profissao = profissao
        self._saldo = saldo
        self._ativo = False
