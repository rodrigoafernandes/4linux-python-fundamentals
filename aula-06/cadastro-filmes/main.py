from repositorio import delete, find_all, find_by_filter, save


def main():
    menu = {
        '1': listar_filmes,
        '2': filtrar_filmes,
        '3': cadastrar_filme,
        '4': excluir_filme,
        '5': sair
    }

    while True:
        menu_item = input('Selecione a operação desejada:\n'
                          '1)Listar todos os filmes\t2)Buscar filme por filtro\n'
                          '3)Cadastrar novo filme\t4)Excluir filme\n'
                          '5)Sair\n')

        if menu_item in menu.keys():
            menu[menu_item]()
        else:
            print('Opção inválida')


def listar_filmes():
    print(find_all())


def filtrar_filmes():

    filtros = {
        '1': 'title',
        '2': 'year',
        '3': 'director',
        '4': 'writer',
        '5': 'actors'
    }

    filtro = input('Selecione um campo para realizar o filtro:\n'
                   '1)Título\t2)Ano de lançamento\t3)Diretor(a)\t4)Escritor(es)\t5)Ator')
    valor = input('Digite o valor a ser pesquisado:\n')

    print(find_by_filter(filtros[filtro], valor))


def cadastrar_filme():
    title = input('Digite o nome do filme:\n')
    year = input('Digite o ano de lançamento do filme:\n')
    director = input('Digite o diretor(a) do filme:\n')
    writer = input('Digite o(s) escritor(es) do filme:\n')
    actors = input('Digite os atores do filme:\n')
    filme = (title, year, director, writer, actors)

    save(filme)


def excluir_filme():
    title = input('Digite o nome do filme que deseja excluir:\n')
    delete(title)


def sair():
    print('Obrigado por utilizar nosso sistema!')
    exit()


if __name__ == '__main__':
    main()
