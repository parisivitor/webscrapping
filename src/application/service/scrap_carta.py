from application.service.shared.scrapper import Scrapper
from domain.aerodromo.scrap_interface.i_scrap_carta import IScrapCarta
from bs4 import BeautifulSoup

class ScrapCarta(IScrapCarta):

    @staticmethod
    def get_cartas(input: str):
        print('Fazendo scraping para pegar Cartas Disponiveis...')
        scrapper = Scrapper()
        page, soup = scrapper.scraping('https://aisweb.decea.mil.br?i=cartas')
        input_icao = page.locator('input[name="icaocode"]')
        input_icao.fill(input)
        input_icao.press('Enter')
        page.wait_for_load_state('load')

        soup = BeautifulSoup(page.content(), 'html.parser')
        cartas = soup.find_all('tr')
        cartas = [[el_cart.string.strip() if el_cart.string else el_cart.text.strip().split('\n') for el_cart in carta.find_all('td')[2:7]] for carta in cartas[1:]]
        scrapper.close()
        return cartas
