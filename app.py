from classes import jogo

jogo_praca = jogo('praça', 'Gourmet')
jogo_praca.receber_avaliacao('Gui', 10)
jogo_praca.receber_avaliacao('Lais', 8)
jogo_praca.receber_avaliacao('Emy', 2)

def main():
    jogo_praca.listar_jogos()

if __name__ == '__main__':
    main()