from persistencia import Database
from negocio import CinemaService
from apresentacao import CinemaUI

if __name__ == "__main__":
    db = Database()
    cinema_service = CinemaService(db)
    cinema_ui = CinemaUI(cinema_service)

    cinema_ui.menu_principal()
