from cartas import Cartas
from taf_metar import TafMetar
from sol import Sol
import time

import threading
import queue

class AerodromoFacade():
    _sol: str
    _taf_metar: str
    _cartas: str
    _icao: str

    def __init__(self, icao: str) -> None:
        # self._icao = icao.upper()
        # self._sol =  Sol(self._icao)
        # self._taf_metar = TafMetar(self._icao)
        # self._cartas = Cartas(self._icao)

        self._icao = icao.upper()
        self._sol = None
        self._taf_metar = None
        self._cartas = None

        result_queue = queue.Queue()

        threads = []
        threads.append(threading.Thread(target=self.init_sol, args=(result_queue,)))
        threads.append(threading.Thread(target=self.init_taf_metar, args=(result_queue,)))
        threads.append(threading.Thread(target=self.init_cartas, args=(result_queue,)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        # Obtenha os resultados da fila e atribua às variáveis
        self._sol = result_queue.get()
        self._taf_metar = result_queue.get()
        self._cartas = result_queue.get()

    def init_sol(self, result_queue):
        result_queue.put(Sol(self._icao))

    def init_taf_metar(self, result_queue):
        result_queue.put(TafMetar(self._icao))

    def init_cartas(self, result_queue):
        result_queue.put(Cartas(self._icao))

    # def get_aerodromo_sunset_sunrise(self):
    #     return self._sol

    # def get_aerodromo_taf_metar(self):
    #     return self._taf_metar

    # def get_aerodromo_cartas(self):
    #     return self._cartas


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
    icao =  input('Digite o ICAO do aeródromo que deja pesquisar: ')
    if len(icao) != 4:
         print(f"Aeródromo é um acronimo de 4 letras\n  O digitado('{icao}') contaim {len(icao)} letras")
         icao =  input('Digite o ICAO aerodromo que deja pesquisar: ')

    start_time = time.time()
    aerodromo = AerodromoFacade(icao)
    end_time = time.time()
    total_time = end_time - start_time
    print(aerodromo)
    print(f"Tempo total de execução: {total_time} segundos")
