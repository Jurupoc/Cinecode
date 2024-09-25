class ServicoReservas:
    def __init__(self, servico_sessoes):
        self.servico_sessoes = servico_sessoes

    def reservar_assento(self, id_sessao, qtd_assentos):
        sessao = self.servico_sessoes.obter_sessao_por_id(id_sessao)
        if sessao and sessao.assentos_disponiveis >= qtd_assentos:
            sessao.assentos_disponiveis -= qtd_assentos
            return True
        return False
