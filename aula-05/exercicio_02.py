numbers = []


def main():

    menu = {
        '1': adiciona_item,
        '2': exibe_lista,
        '3': imprime_menor_valor,
        '4': imprime_maior_valor,
        '5': imprime_menor_valor_par,
        '6': imprime_maior_valor_par,
        '7': imprime_menor_valor_impar,
        '8': imprime_maior_valor_impar,
        '9': exit
    }

    while True:
        opt = input('Informe a operação desejada:\n1)Incluir número na lista\t2)Imprimir items da lista'
                    '\t3)Verificar o menor valor na lista\t4)Verificar o maior valor na lista\t'
                    '\t5)Verificar o menor valor par\t6)Verificar o maior valor par\t'
                    '\t7)Verificar o menor valor impar\t8)Verificar o maior valor impar\t9)Sair\n')
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


def imprime_menor_valor_par(numbers):
    print(retorna_menor_numero_par(numbers))


def imprime_maior_valor_par(numbers):
    print(retorna_maior_numero_par(numbers))


def imprime_menor_valor_impar(numbers):
    print(retorn_menor_numero_impar(numbers))


def imprime_maior_valor_impar(numbers):
    print(retorna_maior_numero_impar(numbers))


def retorna_menor_valor(numbers):
    numbers.sort()
    return numbers[0]


def retorna_maior_valor(numbers):
    numbers.sort(reverse=True)
    return numbers[0]


def retorna_menor_numero_par(numbers):
    pares = []

    for num in numbers:
        if num % 2 == 0:
            pares.append(num)

    pares.sort()

    return pares[0]


def retorna_maior_numero_par(numbers):
    pares = []

    for num in numbers:
        if num % 2 == 0:
            pares.append(num)

    pares.sort(reverse=True)

    return pares[0]


def retorn_menor_numero_impar(numbers):
    impares = []

    for num in numbers:
        if num % 2 != 0:
            impares.append(num)

    impares.sort()

    return impares[0]


def retorna_maior_numero_impar(numbers):
    impares = []

    for num in numbers:
        if num % 2 != 0:
            impares.append(num)

    impares.sort(reverse=True)

    return impares[0]


if __name__ == '__main__':
    main()
