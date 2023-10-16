from domain.aerodromo.scrap_interface.i_scrap_carta import IScrapCarta
import pandas as pd
from typing import List


class Cartas():
    icao: str
    cartas: List

    def __init__(self, input, scrap_service: IScrapCarta) -> None:
        self.icao = input
        self.cartas = scrap_service.get_cartas(input)


    def __str__(self):
        df = pd.DataFrame(self.cartas, columns=['Tipo', 'Carta', 'Amdt', 'Data da Efetivação', 'Uso'])
        return df.to_string(index=False)

if __name__ == "__main__":
    input = 'SBBR'
    cartas = Cartas(input)
    print(cartas)
