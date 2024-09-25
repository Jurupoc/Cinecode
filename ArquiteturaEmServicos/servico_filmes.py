class Filme:
    def __init__(self, id_filme, titulo, duracao, classificacao):
        self.id_filme = id_filme
        self.titulo = titulo
        self.duracao = duracao
        self.classificacao = classificacao


class ServicoFilmes:
    def __init__(self):
        self.filmes = []

    def adicionar_filme(self, titulo, duracao, classificacao):
        id_filme = len(self.filmes) + 1
        filme = Filme(id_filme, titulo, duracao, classificacao)
        self.filmes.append(filme)
        return filme

    def listar_filmes(self):
        return self.filmes

    def obter_filme_por_id(self, id_filme):
        for filme in self.filmes:
            if filme.id_filme == id_filme:
                return filme
        return None
