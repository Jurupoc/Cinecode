class Filme:
    def __init__(self, id_filme, titulo, duracao, classificacao):
        self.id_filme = id_filme
        self.titulo = titulo
        self.duracao = duracao
        self.classificacao = classificacao


class Sessao:
    def __init__(self, id_sessao, id_filme, horario, total_assentos):
        self.id_sessao = id_sessao
        self.id_filme = id_filme
        self.horario = horario
        self.total_assentos = total_assentos
        self.assentos_disponiveis = total_assentos


class Database:
    def __init__(self):
        self.filmes = []
        self.sessoes = []

    def adicionar_filme(self, filme):
        self.filmes.append(filme)

    def listar_filmes(self):
        return self.filmes

    def adicionar_sessao(self, sessao):
        self.sessoes.append(sessao)

    def listar_sessoes(self):
        return self.sessoes
