class CinemaUI:
    def __init__(self, cinema_service):
        self.cinema_service = cinema_service

    def menu_principal(self):
        while True:
            print("\nSistema de Gerenciamento de Cinema")
            print("1. Adicionar Filme")
            print("2. Listar Filmes")
            print("3. Adicionar Sessão")
            print("4. Listar Sessões")
            print("5. Reservar Assento")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar_filme()
            elif opcao == "2":
                self.listar_filmes()
            elif opcao == "3":
                self.adicionar_sessao()
            elif opcao == "4":
                self.listar_sessoes()
            elif opcao == "5":
                self.reservar_assento()
            elif opcao == "0":
                print("Encerrando sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def adicionar_filme(self):
        titulo = input("Título do Filme: ")
        duracao = input("Duração (em minutos): ")
        classificacao = input("Classificação: ")
        self.cinema_service.adicionar_filme(titulo, duracao, classificacao)
        print(f"Filme '{titulo}' adicionado com sucesso!")

    def listar_filmes(self):
        filmes = self.cinema_service.listar_filmes()
        if filmes:
            for filme in filmes:
                print(f"ID: {filme.id_filme} - Título: {filme.titulo} - Duração: {filme.duracao}min - Classificação: {filme.classificacao}")
        else:
            print("Nenhum filme cadastrado.")

    def adicionar_sessao(self):
        id_filme = int(input("ID do Filme: "))
        horario = input("Horário da Sessão (HH:MM): ")
        total_assentos = int(input("Total de Assentos: "))
        self.cinema_service.adicionar_sessao(id_filme, horario, total_assentos)
        print("Sessão adicionada com sucesso!")

    def listar_sessoes(self):
        sessoes = self.cinema_service.listar_sessoes()
        if sessoes:
            for sessao in sessoes:
                filme = self.cinema_service.obter_filme_por_id(sessao.id_filme)
                print(f"Sessão ID: {sessao.id_sessao} - Filme: {filme.titulo} - Horário: {sessao.horario} - Assentos Disponíveis: {sessao.assentos_disponiveis}")
        else:
            print("Nenhuma sessão cadastrada.")

    def reservar_assento(self):
        id_sessao = int(input("ID da Sessão: "))
        qtd_assentos = int(input("Quantidade de assentos a reservar: "))
        if self.cinema_service.reservar_assento(id_sessao, qtd_assentos):
            print("Reserva realizada com sucesso!")
        else:
            print("Não foi possível realizar a reserva. Verifique a disponibilidade de assentos.")
