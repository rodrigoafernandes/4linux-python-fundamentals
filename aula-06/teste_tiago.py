from random import shuffle

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
combinacoes = []

def main():
    tentativas = 0
    while len(combinacoes) < 100:
        tentativas += 1
        aux = lista.copy()
        embaralha_lista(aux)
        add_lista_to_combinacoes(aux, combinacoes)
    print(tentativas)


def embaralha_lista(lista):
    shuffle(lista)


def add_lista_to_combinacoes(lista, combinacoes):
    if lista not in combinacoes:
        combinacoes.append(lista)


if __name__ == '__main__':
    main()
