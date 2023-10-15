from domain.shared.scrapper import Scrapper
from bs4 import BeautifulSoup
import pandas as pd
from typing import List


class Cartas(Scrapper):
    url: str = 'https://aisweb.decea.mil.br?i=cartas'
    icao: str
    cartas: List

    def __init__(self, input) -> None:
        super().__init__()
        self.icao = input
        self.cartas = self.get_cartas()
        self.close()


    def get_cartas(self):
        print('Fazendo scraping para pegar Cartas Disponiveis...')
        page, soup = self.scraping(self.url)
        input_icao = page.locator('input[name="icaocode"]')
        input_icao.fill(self.icao)
        input_icao.press('Enter')
        page.wait_for_load_state('load')

        soup = BeautifulSoup(page.content(), 'html.parser')
        cartas = soup.find_all('tr')
        return self.serializer(cartas)

    @staticmethod
    def serializer(cartas):
       return [[el_cart.string.strip() if el_cart.string else el_cart.text.strip().split('\n') for el_cart in carta.find_all('td')[2:7]] for carta in cartas[1:]]


    def __str__(self):
        df = pd.DataFrame(self.cartas, columns=['Tipo', 'Carta', 'Amdt', 'Data da Efetivação', 'Uso'])
        return df.to_string(index=False)

if __name__ == "__main__":
    input = 'SBBR'
    cartas = Cartas(input)
    print(cartas)
