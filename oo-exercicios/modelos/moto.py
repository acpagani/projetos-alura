from modelos.veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self):
        prefix = super().__str__()
        return f"{prefix}, Tipo: {self._tipo}"