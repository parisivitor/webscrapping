from domain.shared.scrapper import Scrapper
import pytaf
from translate import Translator
from concurrent.futures import ThreadPoolExecutor

class TafMetar(Scrapper):
    icao: str
    metar_code: str
    metar_text: str
    metar_text_pt: str
    taf_code: str
    taf_text: str
    taf_text_pt: str


    def __init__(self, icao) -> None:
        super().__init__()
        self.icao = icao
        print('Fazendo scraping para pegar TAF/METAR...')
        self.metar_code , self.taf_code = self.get_taf_metar()
        self.close()
        if self.metar_code and self.taf_code:
            with ThreadPoolExecutor(max_workers=2) as executor:
                print('Decodificando e Traduzindo METAR...')
                self.metar_text = self.decode(self.metar_code)
                metar_text_pt = executor.submit(self.translate, metar=True)

                print('Decodificando e Traduzindo TAF...')
                self.taf_text = self.decode(self.taf_code)
                taf_text_pt = executor.submit(self.translate, taf=True)

                self.taf_text_pt = taf_text_pt.result()
                self.metar_text_pt = metar_text_pt.result()

        elif self.metar_code:
            self.metar_text = self.decode(self.metar_code)
            self.metar_text_pt = self.translate(metar=True)

        elif self.taf_code:
            self.taf_text = self.decode(self.taf_code)
            self.taf_text_pt = self.translate(taf=True)


    def get_taf_metar(self):
        url = f'https://aisweb.decea.mil.br?i=aerodromos&codigo={self.icao}'
        _, soup = self.scraping(url)

        metar = soup.find('h5', string='METAR').next_sibling.next_sibling.text
        taf = soup.find('h5', string='TAF').next_sibling.next_sibling.text

        metar_code = f"METAR {self.icao} {metar}" if metar else None
        taf_code = f"TAF {self.icao} {taf}" if taf else None

        return metar_code, taf_code


    def decode(self, code):
        code = pytaf.TAF(code)
        return pytaf.Decoder(code).decode_taf()


    def translate(self, taf=False, metar=False):
        translator = Translator(to_lang='pt')

        if taf:
            taf = self.taf_text.strip().split('\n')
            taf01 = '\n '.join(taf[:6])
            taf02 = '\n '.join(taf[6:12])
            taf03 = '\n '.join(taf[12:])

            taf01 = translator.translate(taf01)
            taf02 = translator.translate(taf02)
            taf03 = translator.translate(taf03)

            return  taf01 + taf02 + taf03
        else:
            return  translator.translate(self.metar_text)

    def __str__(self) -> str:
        if self.metar_code:
            metar_info = (
               f"METAR: {self.metar_code}\n" +
                ("\n Utilização maxima da api de tradução En -> pt-BR atingido no dia! \n\n" +
                f"METAR: {self.metar_text} \n" if 'MYMEMORY' in self.metar_text_pt else f"Traducao: {self.metar_text_pt}")
            )
        else:
            metar_info = 'Infelizmente esse Aeródromo não contem METAR \n'

        if self.taf_code:
            taf_info = (
                f"TAF: {self.taf_code}\n" +
                ("\n Utilização maxima da api de tradução En -> pt-BR atingido no dia! \n\n" +
                f"Decode: {self.taf_text} \n" if 'MYMEMORY' in self.taf_text_pt else f"Traducao: {self.taf_text_pt}")
            )
        else:
            taf_info = 'Infelizmente esse Aeródromo não contem TAF \n'

        return '-' * 120 + "\n" + metar_info + '-' * 120 + "\n" + taf_info

if __name__ == "__main__":
    input = 'SJAS'
    taf_metar = TafMetar(input)
    print(taf_metar)
