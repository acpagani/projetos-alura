class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return (f'Dados Cadastrais: \n'
                f'Nome: {self._nome}\n'
                f'Idade: {self._idade}\n'
                f'Profissão: {self._profissao}')

    def aniversario(self):
        self._idade += 1

    def saudacao(self):
        if self._profissao:
            return print(f'Olá! Me chamo {self._nome}, tenho {self._idade} anos e trabalho como {self._profissao}')
        else:
            return print(f'Olá! Me chamo {self._nome} e tenho {self._idade} anos')


roberto = Pessoa('Roberto', 25, 'Motorista')
roberto.aniversario()

claudia = Pessoa('Claudia', 20)
claudia.aniversario()
claudia.saudacao()
roberto.saudacao()
