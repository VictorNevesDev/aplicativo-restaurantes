from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')


bebida_suco = Bebida('Suco de Abacaxi', 5.0, 'grande')

# Aplicando desconto
bebida_suco.aplicar_desconto()

prato_peixe = Prato('Peixão', 2.0, 'O melhor peixe da cidade')

# Aplicando desconto
prato_peixe.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_peixe)

restaurante_praca.receber_avaliacao('Victor', 4)
restaurante_praca.receber_avaliacao('Leticia', 2)

#restaurante_praca.alternar_estado()

def main():
    restaurante_praca.exibir_cardapio()
    Restaurante.listar_restaurantes()
    

if __name__ == '__main__':
    main()