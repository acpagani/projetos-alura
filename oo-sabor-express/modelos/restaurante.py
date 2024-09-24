from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return self._nome

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante":<20} | {"Categoria":<20} | {"Avaliação":<20} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome:<20} | {restaurante.categoria:<20} '
                  f'| {restaurante.media_avaliacoes:<20} | {restaurante.ativo:}')

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        media = round(sum(avaliacao.nota for avaliacao in self._avaliacao) / len(self._avaliacao), 1)
        return media

    def add_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f"Cardapio do restaurante {self.nome}\n")
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, "descricao"):
                print(f"{i}: {item.nome} | {item.preco} | {item.descricao}")
            else:
                print(f"{i}: {item.nome} | {item.preco} | {item.tamanho}")