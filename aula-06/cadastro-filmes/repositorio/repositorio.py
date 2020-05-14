import csv
import pathlib


def find_all():
    with open(f'{pathlib.Path(__file__).parent.absolute()}/csv/filmes.csv', 'r') as arquivo:
        content = csv.reader(arquivo, delimiter=';')
        next(content)
        filmes = []
        for linha in content:
            filmes.append(convert_line_to_json(linha))

    return filmes


def find_by_filter(filtro, valor):
    result = []
    filmes = find_all()

    for filme in filmes:
        if filme[filtro].upper() == valor.upper():
            result.append(filme)

    return result


def save(filme):
    with open(f'{pathlib.Path(__file__).parent.absolute()}/csv/filmes.csv', 'a+') as arquivo:
        arquivo.write(f'\n{filme[0]};{filme[1]};{filme[2]};{filme[3]};{filme[4]}')
        arquivo.close()


def delete(title):
    movies = find_all()

    for movie in movies:
        if movie['title'].upper() == title.upper():
            movies.remove(movie)

    with open(f'{pathlib.Path(__file__).parent.absolute()}/csv/filmes.csv', 'w') as arquivo:
        arquivo.write(f'titulo;ano;diretor(a);roteirista;atores')

        for movie in movies:
            arquivo.write(f'\n{movie["title"]};{movie["year"]};{movie["director"]};{movie["writer"]};{movie["actors"]}')


def convert_line_to_json(linha):
    return {"title": linha[0], "year": linha[1], "director": linha[2], "writer": linha[3], "actors": linha[4]}
