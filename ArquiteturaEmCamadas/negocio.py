from persistencia import Filme, Sessao

class CinemaService:
    def __init__(self, database):
        self.database = database

    def adicionar_filme(self, titulo, duracao, classificacao):
        id_filme = len(self.database.filmes) + 1
        filme = Filme(id_filme, titulo, duracao, classificacao)
        self.database.adicionar_filme(filme)

    def listar_filmes(self):
        return self.database.listar_filmes()

    def adicionar_sessao(self, id_filme, horario, total_assentos):
        filme = self.obter_filme_por_id(id_filme)
        if filme:
            id_sessao = len(self.database.sessoes) + 1
            sessao = Sessao(id_sessao, id_filme, horario, total_assentos)
            self.database.adicionar_sessao(sessao)

    def listar_sessoes(self):
        return self.database.listar_sessoes()

    def reservar_assento(self, id_sessao, qtd_assentos):
        sessao = self.obter_sessao_por_id(id_sessao)
        if sessao and sessao.assentos_disponiveis >= qtd_assentos:
            sessao.assentos_disponiveis -= qtd_assentos
            return True
        return False

    def obter_filme_por_id(self, id_filme):
        for filme in self.database.filmes:
            if filme.id_filme == id_filme:
                return filme
        return None

    def obter_sessao_por_id(self, id_sessao):
        for sessao in self.database.sessoes:
            if sessao.id_sessao == id_sessao:
                return sessao
        return None
