from modelos.veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas

    def __str__(self):
        prefix = super().__str__()
        return f"{prefix}, Portas: {self._portas}"
