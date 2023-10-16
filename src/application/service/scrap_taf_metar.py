from application.service.shared.scrapper import Scrapper
from domain.aerodromo.scrap_interface.i_scrap_taf_metar import IScrapTafMetar

class ScrapTafMetar(IScrapTafMetar):

    @staticmethod
    def get_taf_metar(icao):
        url = f'https://aisweb.decea.mil.br?i=aerodromos&codigo={icao}'
        scrapper = Scrapper()
        _, soup = scrapper.scraping(url)

        metar = soup.find('h5', string='METAR').next_sibling.next_sibling.text
        taf = soup.find('h5', string='TAF').next_sibling.next_sibling.text

        metar_code = f"METAR {icao} {metar}" if metar else None
        taf_code = f"TAF {icao} {taf}" if taf else None
        scrapper.close()
        return metar_code, taf_code
