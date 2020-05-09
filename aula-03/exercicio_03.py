opcao = 0
pessoas = []
while opcao > -1:
    try:
        opcao = int(input(f'Digite uma opção:\n1) Adicionar Pessoa\t2) Mostrar idade das pessoas do estado de SP\t3) Sair\n'))
    except ValueError:
        print('Opcao errada. Selecione novamente.')
        opcao = 0

    if opcao == 1:
        try:
            nome = input('Digite o nome da pessoa: ')
            idade = int(input('Digite a idade da pessoa: '))
            sexo = input('Digite o sexo da pessoa: ')
            cpf = input('Digite o cpf da pessoa: ')
            estado = input('Digite o estado da pessoa: ')
            pessoas.append({"nome": nome, "idade": idade, "sexo": sexo, "cpf": cpf, "estado": estado})
        except ValueError:
            print('Valor inserido inválido. Por favor, tente novamente.')
            opcao = 0

    if opcao == 2:
        for pessoa in pessoas:
            if pessoa['estado'].upper() == 'SP': 
                print(pessoa['idade'])

    if opcao == 3:
        print('Selecionado sair. Obrigado por utilizar nosso sistema!')
        break
