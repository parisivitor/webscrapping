from domain.aerodromo.scrap_interface.i_scrap_sol import IScrapSol
from typing import Dict

class Sol():
    infos: Dict
    _icao_is_valid: bool

    def __init__(self, icao, scrap_sol: IScrapSol):
        super().__init__()
        self.infos, self._icao_is_valid = scrap_sol.get_hour_sunset_sunrise(icao)

    def icao_is_valid(self):
        return self._icao_is_valid

    def __str__(self):
        return(
            f"{'-'*104}\n"
            f"{' '*20}   Data: {self.infos.get('Data')}, Dia da semana: {self.infos.get('Dia da Semana')} \n"
            f"{' '*20}   Horarios de Nascer e Por do sol: \n"
            f"{' '*20}   Nascer do sol: {self.infos.get('Sunrise')}, Por do Sol: {self.infos.get('Sunset')} \n\n"
        )

if __name__ == "__main__":
    input = 'asdd'
    sol = Sol(input)
    print(sol)
