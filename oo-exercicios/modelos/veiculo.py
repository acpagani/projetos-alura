class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        status = 'ligado' if self._ligado else 'desligado'
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Lig/Deslig: {status}"
