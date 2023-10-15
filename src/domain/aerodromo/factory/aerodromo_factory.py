from domain.aerodromo.entities.cartas import Cartas
from domain.aerodromo.entities.taf_metar import TafMetar
from domain.aerodromo.entities.sol import Sol

from concurrent.futures import ThreadPoolExecutor

import time
class AerodromoFactory():

    @staticmethod
    def create_aerodromo(icao: str):
        icao = icao.upper()
        sol =  Sol(icao)

        if sol.icao_is_valid():
            with ThreadPoolExecutor(max_workers=2) as executor:
                future_taf_metar = executor.submit(TafMetar, icao)
                future_cartas = executor.submit(Cartas, icao)

                taf_metar = future_taf_metar.result()
                cartas = future_cartas.result()

            return Aerodromo(icao, sol, taf_metar, cartas)
        else:
            return False



class Aerodromo:
    def __init__(self, icao, sol, taf_metar, cartas):
        self._icao = icao
        self._sol = sol
        self._taf_metar = taf_metar
        self._cartas = cartas

    def __str__(self):
        info_aerodromo = (
            f"{'-'*104}\n"
            f"{' '*20}   Informacoes sobre o Aeródromo de {self._icao} \n\n"
            f"{str(self._sol)} \n\n"
            f"{' '*104}\n"
            f"{' '*20}   Taf e Metar: \n"
            f"{str(self._taf_metar)} \n\n"
            f"{'-'*104}\n"
            f"{' '*20}   Cartas Disponiveis: \n"
            f"{str(self._cartas)} \n\n"
            f"{'-'*104}\n"
        )
        return info_aerodromo


if __name__ == "__main__":
    start_time = time.time()
    aerodromo = AerodromoFactory.create_aerodromo('SBMT')
    end_time = time.time()
    total_time = end_time - start_time
    print(aerodromo)
    print(f"Tempo total de execução: {total_time} segundos")
