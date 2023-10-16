from application.service.shared.scrapper import Scrapper
from domain.aerodromo.scrap_interface.i_scrap_sol import IScrapSol
from bs4 import BeautifulSoup
import datetime

class ScrapSol(IScrapSol):

    @staticmethod
    def get_hour_sunset_sunrise(icao):
        url = 'https://aisweb.decea.mil.br/?i=aerodromos&p=sol'
        scrapper = Scrapper()
        page, _ = scrapper.scraping(url)

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

        icao_is_valid = not page.get_by_text('O aeródromo não foi encontrado.').is_visible()

        if not icao_is_valid:
            scrapper.close()
            return None, False

        thead = page.locator('thead').inner_text().strip().split('\t')
        tbody = page.locator('tbody').inner_text().strip().split('\t')
        scrapper.close()

        return dict(zip(thead, tbody)), icao_is_valid
