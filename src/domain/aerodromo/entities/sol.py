from domain.shared.scrapper import Scrapper
import datetime
from typing import Dict


class Sol(Scrapper):
    infos: Dict
    _icao_is_valid: bool

    def __init__(self, icao):
        super().__init__()
        self.infos = self.get_hour_sunset_sunrise(icao)
        self.close()

    def get_hour_sunset_sunrise(self, icao):
        url = 'https://aisweb.decea.mil.br/?i=aerodromos&p=sol'
        page, _ = self.scraping(url)

        print('Fazendo scraping para pegar Nascer e por do Sol...')
        input_icao = page.locator('input[name="icaocode"]')
        input_icao.fill(icao)

        today = datetime.date.today().strftime('%d%m%Y')
        input_initial_date = page.locator('input[name="dt_i"]')
        input_initial_date.fill(today)

        input_end_date = page.locator('input[name="dt_f"]')
        input_end_date.fill(today)

        input_end_date.press('Enter')
        page.wait_for_load_state('load')

        self._icao_is_valid =  not page.get_by_text('O aeródromo não foi encontrado.').is_visible()

        if not self._icao_is_valid:
            return

        thead = page.locator('thead').inner_text().strip().split('\t')
        tbody = page.locator('tbody').inner_text().strip().split('\t')
        return dict(zip(thead, tbody))

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
