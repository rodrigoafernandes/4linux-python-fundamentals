numbers = []


def main():

    menu = {
        '1': adiciona_item,
        '2': exibe_lista,
        '3': retorna_menor_valor,
        '4': retorna_maior_valor,
        '5': exit
    }

    while True:
        opt = input('Informe a operação desejada:\n1)Incluir número na lista\t2)Imprimir items da lista'
                    '\t3)Verificar o menor valor na lista\t4)Verificar o maior valor na lista\t5)Sair\n')
        if opt in menu.keys():
            menu[opt](numbers)
        else:
            print(f'Opção {opt} inválida.')

def adiciona_item(numbers):
    numbers.append(int(input('Digite o número desejado: ')))


def exibe_lista(numbers):
    print(numbers)


def imprime_menor_valor(numbers):
    print(retorna_menor_valor(numbers))


def imprime_maior_valor(numbers):
    print(retorna_maior_valor(numbers))


def retorna_menor_valor(numbers):
    numbers.sort()
    return numbers[0]


def retorna_maior_valor(numbers):
    numbers.sort(reverse=True)
    return numbers[0]


if __name__ == '__main__':
    main()
