from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')
restaurante_praca.add_cardapio(bebida_suco)
restaurante_praca.add_cardapio(prato_paozinho)


def main():
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
