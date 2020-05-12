pessoas = []


def main():
    opcoes = {
            '1': cadastrar_usuario,
            '2': mostrar_registros,
            '3': filtrar_por_estado,
            '4': exit
    }

    opcao = 0

    while opcao > -1:
        try:
            opcao = int(input('Digite uma opção:\n1) Adicionar Pessoa'
                              '\t2) Mostrar idade das pessoas do estado de SP\t3) Filtrar por Estado'
                              '\t4) Sair\n'))

            if str(opcao) in opcoes.keys():
                opcoes[str(opcao)](pessoas)
            else:
                print(f'Opcao {opcao} invalida. Selecione novamente.')
                opcao = 0
        except ValueError:
            print('Opcao errada. Selecione novamente.')
            opcao = 0


def cadastrar_usuario(pessoas):
    pessoas.append({"nome": input('Digite o nome da pessoa: '), "idade": int(input('Digite a idade da pessoa: ')), "sexo": input('Digite o sexo da pessoa: '), "cpf": input('Digite o cpf da pessoa: '), "estado": input('Digite o estado da pessoa: ')})


def mostrar_registros(pessoas):
    for pessoa in pessoas:
        print(pessoa)


def filtrar_por_estado(pessoas):
    uf = input('Digite o estado que deseja filtrar: ')
    for pessoa in pessoas:
        if pessoa['estado'].upper() == uf.upper():
            print(pessoa)


if __name__ == '__main__':
    main()
