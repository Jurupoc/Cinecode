class Sessao:
    def __init__(self, id_sessao, id_filme, horario, total_assentos):
        self.id_sessao = id_sessao
        self.id_filme = id_filme
        self.horario = horario
        self.total_assentos = total_assentos
        self.assentos_disponiveis = total_assentos


class ServicoSessoes:
    def __init__(self):
        self.sessoes = []

    def adicionar_sessao(self, id_filme, horario, total_assentos):
        id_sessao = len(self.sessoes) + 1
        sessao = Sessao(id_sessao, id_filme, horario, total_assentos)
        self.sessoes.append(sessao)
        return sessao

    def listar_sessoes(self):
        return self.sessoes

    def obter_sessao_por_id(self, id_sessao):
        for sessao in self.sessoes:
            if sessao.id_sessao == id_sessao:
                return sessao
        return None
